import sys, requests, os
from PySide2.QtWidgets import *
from PySide2.QtGui import QImage, QPixmap
from PIL import Image
from ui_pixivchecker import Ui_PixivChecker

class PixivChecker(QMainWindow, Ui_PixivChecker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #配置数据
        self.pid = "0"
        self.MultiPage = False
        self.Page = 0
        self.PicType = "png"
        self.Mirror = True

        self.editPage.setEnabled(False)
        self.SavePicture.setEnabled(False)
        self.ReloadPicture.setEnabled(False)

        self.PIDSubmit.clicked.connect(self.submit)
        self.About.clicked.connect(self.about)
        self.SavePicture.clicked.connect(self.downloadPic)
        self.ReloadPicture.clicked.connect(self.reloadPic)
        self.isMultiPage.stateChanged.connect(self.changeMultiPage)

        self.show()
    
    def submit(self): # 组合图片地址
        self.PictureView.setText("图片获取中，这可能要一段时间")
        self.readInfo()
        self.disabled_sth(False)
        self.url = "https://pixiv."
        if self.Mirror:
            self.url += "re/"
        else:
            self.url += "cat/"
        
        self.url += str(self.pid)
        if self.MultiPage:
            self.url += "-"
            self.url += str(self.Page)
        self.url += "."
        self.url += self.PicType

        self.showPicture(self.url, self.PicType)
    
    def disabled_sth(self, state):
        if state == False:
            self.SavePicture.setEnabled(False)
            self.ReloadPicture.setEnabled(False)
            self.PIDSubmit.setEnabled(False)
            self.About.setEnabled(False)
            self.isMirror.setEnabled(False)
            self.isMultiPage.setEnabled(False)
            self.editPage.setEnabled(False)
            self.editPID.setEnabled(False)
            self.pngButton.setEnabled(False)
            self.jpgButton.setEnabled(False)
            self.gifButton.setEnabled(False)
        else:
            self.PIDSubmit.setEnabled(True)
            self.About.setEnabled(True)
            self.isMirror.setEnabled(True)
            self.isMultiPage.setEnabled(True)
            if self.MultiPage:
                self.editPage.setEnabled(True)
            else:
                self.editPage.setEnabled(False)
            self.editPID.setEnabled(True)
            self.pngButton.setEnabled(True)
            self.jpgButton.setEnabled(True)
            self.gifButton.setEnabled(True)

    def changeMultiPage(self):
        if self.isMultiPage.isChecked():
            self.editPage.setEnabled(True)
        else:
            self.editPage.setEnabled(False)
            self.Page = None
    
    def readInfo(self): # 获取信息
        self.pid = self.editPID.text() # 获取PID
        self.MultiPage = self.isMultiPage.isChecked() # 获取是否多张插画
        if self.MultiPage:
            self.Page = self.editPage.text() # 获取页数
        
        # 获取文件格式
        if self.pngButton.isChecked():
            self.PicType = "png"
        if self.jpgButton.isChecked():
            self.PicType = "jpg"
        if self.gifButton.isChecked():
            self.PicType = "gif"
        
        self.Mirror = self.isMirror.isChecked() # 获取是否为镜像
    
    def showPicture(self, url, tp): # 展示图片
        self.img = requests.get(url)
        if self.img.status_code == 404:
            if self.MultiPage:
                QMessageBox.critical(self, "错误", "图片不存在或当前PID不是图集\nError Code: W404")
            else:
                QMessageBox.critical(self, "错误", "图片不存在或当前PID为图集\nError Code: W404")
            self.PictureView.setText("图片将在这里展示...")
        elif self.img.status_code == 403:
            QMessageBox.critical(self, "错误", "服务器拒绝访问，请稍后再试\nError Code: W403")
            self.PictureView.setText("图片将在这里展示...")
        elif self.img.status_code >= 500:
            QMessageBox.critical(self, "错误", "服务器出现错误或已重定向到新网址，请稍后再试或联系作者\nError Code: W50X")
            self.PictureView.setText("图片将在这里展示...")
        else:
            file_name = "file.obj"
            with open(file_name, "wb") as f:
                f.write(self.img.content)

            img4pic = Image.open(file_name)
            w = img4pic.width
            h = img4pic.height

            if w <= h:
                scale = w / h
                h = 375
                w = h * scale
            else:
                scale = h / w
                w = 530
                h = w * scale

            pic = QPixmap(file_name).scaled(w, h)

            self.PictureView.setPixmap(pic)
            #self.PictureView.setScaledContents(True)

            self.SavePicture.setEnabled(True)
            self.ReloadPicture.setEnabled(True)

        self.disabled_sth(True)
    
    def downloadPic(self):
        try:
            ft = "(*." + self.PicType + ")"
            file_path = QFileDialog.getSaveFileName(
                caption="选择文件保存位置", filter=ft)
        except:
            return
        with open(file_path[0], "wb") as f:
            f.write(self.img.content)
        QMessageBox.information(self, "提示", "文件保存成功！")
    
    def reloadPic(self):
        self.showPicture(self.url, self.PicType)
    
    def about(self):
        QMessageBox.information(self, "关于", "Pixiv图片查看\n作者：0x4D2\n版本：r1.0\n2046360988@qq.com")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixivChecker()
    sys.exit(app.exec_())
