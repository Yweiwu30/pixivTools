import sys
import requests
import os
import atexit
import time
import json
import logging
import traceback
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PIL import Image
from threading import Thread, enumerate
from ui_pixivtools import Ui_PixivTools
import win32api, win32con


class PicSignals_r(QObject):
    Line = Signal(QLineEdit, str)
    Pix = Signal(QLabel, QPixmap)
    Err = Signal(QMessageBox, str)


class PixivTools(QMainWindow, Ui_PixivTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        atexit.register(self.delete)
        atexit.register(self.delete_r)

        self.version = "beta-2.2"

        self.PS = PicSignals_r()  # 实例化

         # 日志
        self.log()
        self.logger.info("导入日志模块成功")

        # 配置数据
        self.pid = "0"
        self.MultiPage = False
        self.Page = 0
        self.PicType = "png"
        self.D_PicType = "png"
        self.f_name = "pid"
        self.Mirror = True
        #self.reTry = False
        self.Remember = True
        self.r_mode = "1"
        self.img = None
        self.pidList = []
        self.Error = False

        self.editPage.setEnabled(False)
        self.SavePicture.setEnabled(False)
        self.ReloadPicture.setEnabled(False)
        self.SavePicture_R.setEnabled(False)
        self.ReloadPicture_R.setEnabled(False)

        self.PIDSubmit.clicked.connect(self.submit)
        # self.About.clicked.connect(self.about)
        self.SavePicture.clicked.connect(self.downloadPic)
        self.ReloadPicture.clicked.connect(self.reloadPic)
        self.ResetPicture.clicked.connect(self.resetPic)
        self.isMultiPage.stateChanged.connect(self.changeMultiPage)
        # self.NameSelf.toggled.connect(self.changeNameEdit)
        self.RandomButton.clicked.connect(self.random)
        self.SavePicture_R.clicked.connect(self.downloadPic_r)
        self.ResetPicture_R.clicked.connect(self.resetPic_r)
        self.ReloadPicture_R.clicked.connect(self.reloadPic_r)
        self.Add.clicked.connect(self.addList)
        self.Clean.clicked.connect(self.clearList)
        self.Delete.clicked.connect(self.deleteList)
        self.Download.clicked.connect(self.Download_d)
        self.pictureList.itemClicked.connect(self.clickList)

        self.Delete.setEnabled(False)

        #self.SearchList.addItems(["该功能尚未制作", "如果你有关于搜索的api可以提供（最好不用翻墙）", "并且可以返回pid", "请务必告诉我们！", "联系方式详见\"关于\"一栏"])

        self.About.setText(
            "pixiv工具箱\nversion {}\n作者：0x42D\nhttps://github.com/Yweiwu30\n联系方式：2046360988@qq.com".format(self.version))
        self.PictureView.setText("预览图将在这里展示...")
        self.PictureView_2.setText("预览图将在这里展示...")

        self.label_status = QLabel(self)

        self.PS.Line.connect(self.printInfo)
        self.PS.Pix.connect(self.printPic)
        self.PS.Err.connect(self.printError)
        self.logger.info("配置数据成功")

        self.show()
    
    def log(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        logfile = './log.txt'
        fh = logging.FileHandler(logfile, mode='a')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d][%(threadName)s, %(thread)s] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def catch_exception(func):
        def warp(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                logging.basicConfig(level=logging.WARNING,  
                    filename='./log.txt',  
                    filemode='w',  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  
                logging.error(f"在执行 {func.__name__}时出现错误, args: {args}, kwargs: {kwargs}")
                logging.error(traceback.format_exc())
                win32api.MessageBox(0, "程序出现错误，请查看日志", "错误", win32con.MB_ICONERROR)
        return warp

    def printInfo(self, fd, text):
        fd.setText(text)

    def printPic(self, fd, pic):
        fd.setPixmap(pic)

    def printError(self, fd, text):
        fd.critical(self, "错误", text)

    @catch_exception
    def submit(self):  # 组合图片地址
        print(1/0)
        # self.PictureView.setText("图片获取中，这可能要一段时间")
        self.logger.info("加载网址")
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

        self.showPicture(self.url)

    @catch_exception
    def disabled_sth(self, state):
        if state == False:
            # self.SavePicture.setEnabled(False)
            # self.ReloadPicture.setEnabled(False)
            self.PIDSubmit.setEnabled(False)
            self.About.setEnabled(False)
            self.isMirror.setEnabled(False)
            self.isMultiPage.setEnabled(False)
            self.editPage.setEnabled(False)
            self.editPID.setEnabled(False)
            self.pngButton.setEnabled(False)
            self.jpgButton.setEnabled(False)
            self.gifButton.setEnabled(False)
            self.isRemember.setEnabled(False)
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
            self.isRemember.setEnabled(True)

    @catch_exception
    def changeMultiPage(self):
        if self.isMultiPage.isChecked():
            self.editPage.setEnabled(True)
        else:
            self.editPage.setEnabled(False)
            self.Page = None
            self.editPage.setValue(1)

    @catch_exception
    def readInfo(self):  # 获取信息
        self.logger.info("获取图片")
        self.statusBar.showMessage("获取信息中...")
        self.Remember = self.isRemember.isChecked()
        self.pid = self.editPID.text()  # 获取PID
        self.MultiPage = self.isMultiPage.isChecked()  # 获取是否多张插画
        if self.MultiPage:
            self.Page = self.editPage.text()  # 获取页数

        # 获取文件格式
        if self.pngButton.isChecked():
            self.PicType = "png"
        if self.jpgButton.isChecked():
            self.PicType = "jpg"
        if self.gifButton.isChecked():
            self.PicType = "gif"

        self.Mirror = self.isMirror.isChecked()  # 获取是否为镜像

    @catch_exception
    def showPicture(self, url):  # 展示图片
        self.statusBar.showMessage("加载图片中...")  # 显示状态
        thread = Thread(target=self.requestPic, args=(url))  # 新建线程
        self.logger.info("已新建线程")
        thread.start()
        self.logger.info("当前活跃中线程: {}".format(enumerate()))

    @catch_exception
    def requestPic(self, url):
        self.logger.info("加载图片")
        self.PS.Line.emit(self.PictureView, "加载中，请稍后...")
        self.img = requests.get(url)
        err_info = ""
        if self.img.status_code == 404:  # 检测错误状态
            if self.MultiPage:
                err_info = "图片不存在或当前PID不是图集\nError Code: W404"
            else:
                err_info = "图片不存在或当前PID是图集\nError Code: W404"
        elif self.img.status_code == 403:
            err_info = "服务器拒绝访问，请稍后再试\nError Code: W403"
        elif self.img.status_code == 504:
            err_info = "服务器网关超时，请稍后再试\nError Code: W504"
        elif self.img.status_code == 408: 
            err_info = "服务器请求超时，请稍后再试\nError Code: W408"
        elif self.img.status_code == 503:
            err_info = "图片不存在或服务器目前无法使用\nError Code: W503"
        elif 300 <= self.img.status_code < 400:
            err_info = "服务器出现错误或已重定向到新网址，请稍后再试或联系作者\nError Code: W{}".format(
                str(self.img.status_code))
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

            self.PS.Pix.emit(self.PictureView, pic)
            # self.PictureView.setScaledContents(True)

            self.SavePicture.setEnabled(True)
            self.ReloadPicture.setEnabled(True)

            if self.Remember:
                self.statusBar.showMessage("保存记录中...")
                self.logger.info("保存历史记录")
                self.history = ""
                localtime = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime())

                text = localtime+" | "+self.pid+" " * \
                    (11-len(self.pid))+"| "+str(self.MultiPage) + \
                    " "*(5-len(str(self.MultiPage)))+" | "
                if self.MultiPage:
                    text += str(self.Page)
                try:
                    with open("History_rec.txt", "r", encoding="utf-8") as f:
                        self.history = f.read()
                except:
                    pass

                if self.history[0:21] == "[PIXIV_TOOLS.HISTORY]":
                    pass
                else:
                    with open("History_rec.txt", "w", encoding="utf-8") as f:
                        f.write('''[PIXIV_TOOLS.HISTORY] 
            Time        |     PID    | Multi | Page  \n''')

                f = open("History_rec.txt", "a", encoding="utf-8")
                f.write(text+"\n")
                f.close()

        if err_info != "":
            # self.PS.Err.emit(err_info)
            self.PS.Line.emit(self.PictureView, err_info)
            self.logger.info("网页返回{}, {}".format(self.img.status_code, err_info))

        self.disabled_sth(True)
        self.statusBar.showMessage("完成")

    @catch_exception
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
        self.logger.info("保存文件成功，文件位于{}".format(file_path[0]))

    def reloadPic(self):
        self.showPicture(self.url)

    def resetPic(self):
        self.PictureView.setText("预览图将在这里显示...")

    @catch_exception
    def delete(self):
        self.logger.info("删除缓存数据")
        try:
            os.remove("file.obj")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    @catch_exception
    def readInfo_r(self):  # 获取信息（随机图）
        # 获取文件格式
        if self.Daily.isChecked():
            self.r_mode = "1"
        if self.Monthly.isChecked():
            self.r_mode = "3"
        if self.Weekly.isChecked():
            self.r_mode = "2"

    @catch_exception
    def checkError_r(self, req):
        self.logger.info("检测错误")
        status = False
        self.PS.Line.emit(self.PictureView, "预览图将在这里展示..")
        if req.status_code == 404:
            QMessageBox.critical(self, "错误", "图片不存在\nError Code: R404")
        elif req.status_code == 403:
            QMessageBox.critical(self, "错误", "服务器拒绝访问，请稍后再试\nError Code: R403")
        elif req.status_code == 504:
            QMessageBox.critical(self, "错误", "服务器网关超时，请稍后再试\nError Code: R504")
        elif req.status_code == 408:
            QMessageBox.critical(self, "错误", "服务器请求超时，请稍后再试\nError Code: R408")
        elif req.status_code == 503:
            QMessageBox.critical(self, "错误", "服务器目前无法使用\nError Code: R503")
        elif 300 <= req.status_code < 400:
            QMessageBox.critical(self, "错误", "服务器出现错误或已重定向到新网址，请稍后再试或联系作者\nError Code: R{}".format(
                str(req.status_code)))
        else:
            status = True
        return status

    @catch_exception
    def setEnabled_r(self, stat):
        self.RandomButton.setEnabled(stat)
        self.ReloadPicture_R.setEnabled(stat)
        self.SavePicture_R.setEnabled(stat)
        self.Daily.setEnabled(stat)
        self.Weekly.setEnabled(stat)
        self.Monthly.setEnabled(stat)

    @catch_exception
    def showPicture_r(self, url):  # 展示图片
        self.logger.info("获取图片")
        self.PS.Line.emit(self.PictureView_2, "加载中，请稍后...")
        self.setEnabled_r(False)
        self.statusBar.showMessage("获取信息中...")
        info_r = requests.get(url)

        if self.checkError_r(info_r):
            info_j = info_r.content.decode('utf8').replace("'", '"')
            info = json.loads(info_j)
            #print(info, type(info))
            id = str(info['id'])
            title = info['title']
            tags_l = info['tags']
            tags = str(tags_l).replace("\'", "").replace(
                "[", "").replace("]", "")
            date_n = info['date']
            date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date_n))

            self.PS.Line.emit(self.name, title)
            self.PS.Line.emit(self.date, id)
            self.PS.Line.emit(self.pid_r, date)
            self.PS.Line.emit(self.tag, tags)

            self.logger.info("加载图片")
            self.statusBar.showMessage("加载图片中...")
            self.img_r = requests.get(info['url'])
            if self.checkError_r(self.img_r):
                file_name = "random.obj"
                with open(file_name, "wb") as f:
                    f.write(self.img_r.content)

                img4pic = Image.open(file_name)
                w = img4pic.width
                h = img4pic.height

                if w <= h:
                    scale = w / h
                    h = 300
                    w = h * scale
                else:
                    scale = h / w
                    w = 510
                    h = w * scale

                pic = QPixmap(file_name).scaled(w, h)

                self.PS.Pix.emit(self.PictureView_2, pic)

        self.statusBar.showMessage("完成")
        self.setEnabled_r(True)

    def reloadPic_r(self):
        self.showPicture_r(self.url_r)

    @catch_exception
    def delete_r(self):
        self.logger.info("删除缓存文件")
        try:
            os.remove("random.obj")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    @catch_exception
    def downloadPic_r(self):
        try:
            ft = "(*.png)"
            file_path = QFileDialog.getSaveFileName(
                caption="选择文件保存位置", filter=ft)
        except:
            return
        with open(file_path[0], "wb") as f:
            f.write(self.img_r.content)
        QMessageBox.information(self, "提示", "文件保存成功！")
        self.logger.info("文件保存成功, 位于{}".format(file_path[0]))

    def resetPic_r(self):
        self.PictureView_2.setText("预览图将在这里显示...")

    @catch_exception
    def random(self):
        self.readInfo_r()
        self.url_r = "https://api.pixiv.cx/rank/?format=json&mode="
        self.url_r += self.r_mode
        thread_r = Thread(target=self.showPicture_r, args=(self.url_r,))
        self.logger.info("已新建线程")
        thread_r.start()
        self.logger.info("当前活跃中线程: {}".format(enumerate()))

    def changeNameEdit(self):
        if self.NameSelf.isChecked():
            self.NameEdit.setEnabled(True)
        else:
            self.NameEdit.setEnabled(False)

    @catch_exception
    def Download_d(self):
        if os.path.exists("Pixiv Download") == False:
            os.mkdir("Pixiv Download")
        if self.D_png.isChecked():
            self.D_PicType = "png"
        if self.D_jpg.isChecked():
            self.D_PicType = "jpg"
        if self.D_gif.isChecked():
            self.D_PicType = "gif"
        if self.NamePid.isChecked():
            self.F_name = "pid"
        if self.NameNo.isChecked():
            self.F_name = "No"
        if self.NameSelf.isChecked():
            self.F_name = "self"
        thread_d = Thread(target=self.dl, args=())
        self.logger.info("已新建线程")
        thread_d.start()
        self.logger.info("当前活跃中线程: {}".format(enumerate()))

    @catch_exception
    def dl(self):
        self.suc_count = 0
        self.fail_count = 0
        for y in range(len(self.pidList)):
            i = self.pidList[y]
            self.StatusText.append("({}/{})正在尝试下载图片：{}".format(y+1, len(self.pidList), i))
            mpid = i[:-2:]
            self.Error_nf = False
            a = 1
            self.download_l(mpid, 1, a)
            if self.Error_nf == True:
                self.download_l(i, 0, 0)
                continue
            self.StatusText.append("当前pid为图集")
            while self.Error_nf == False:
                a += 1
                self.StatusText.append("尝试下载第{}页图片".format(a))
                self.download_l(mpid, 1, a)
        self.statusBar.showMessage("完成")
        self.StatusText.append("-"*30+"\n下载完成\n共尝试下载{}次，成功{}次，失败{}次".format(
            self.suc_count+self.fail_count, self.suc_count, self.fail_count))

    @catch_exception
    def download_l(self, pid, mode, num):
        if mode == 1:
            wpid = "{}-{}".format(pid, num)
        else:
            wpid = pid
        url = "https://pixiv.re/{}.png".format(wpid)
        self.logger.info("尝试下载图片: {}".format(wpid))
        self.statusBar.showMessage("正在下载：{}".format(wpid))
        self.img = requests.get(url)
        err_info = ""
        if self.img.status_code == 404:  # 检测错误状态
            if "-" in wpid:
                err_info = "Error Code: W404"
            else:
                err_info = "Error Code: W404"
            self.Error_nf = True
        elif self.img.status_code == 403:
            err_info = "服务器拒绝访问，请稍后再试\nError Code: W403"
        elif self.img.status_code == 504:
            err_info = "服务器网关超时，请稍后再试\nError Code: W504"
        elif self.img.status_code == 408:
            err_info = "服务器请求超时，请稍后再试\nError Code: W408"
        elif self.img.status_code == 503:
            err_info = "图片不存在或服务器目前无法使用\nError Code: W503"
            #self.Error_nf = True
        elif 300 <= self.img.status_code < 400:
            err_info = "服务器出现错误或已重定向到新网址，请稍后再试或联系作者\nError Code: W{}".format(
                str(self.img.status_code))
        else:
            file_name = "{}.png".format(wpid)
            path = "Pixiv Download/{}".format(file_name)
            with open(path, "wb") as f:
                f.write(self.img.content)
            self.StatusText.append("下载成功")
            self.suc_count += 1
            return
        self.Error = True
        self.StatusText.append(err_info)
        self.fail_count += 1

    @catch_exception
    def clickList(self, item):
        self.Delete.setEnabled(True)
        self.logger.debug(item)
        self.clicked_item = self.pictureList.row(item)
        #print(item.text(), self.clicked_item)

    @catch_exception
    def addList(self):
        pid = self.D_pid.text()
        self.pidList.append(pid)
        self.pictureList.addItem(pid)
        self.D_pid.setText("")
    
    @catch_exception
    def deleteList(self):
        try:
            self.pidList.remove(self.pidList[self.clicked_item])
            self.pictureList.takeItem(self.clicked_item)
        except IndexError:
            return None
        try:
            new_selected = self.pictureList.selectedItems()[0]
            if new_selected:
                self.clicked_item = self.pictureList.row(new_selected)
        except IndexError:
            pass
        if self.pidList == []:
            self.Delete.setEnabled(False)

    @catch_exception
    def clearList(self):
        self.pidList = []
        self.pictureList.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo.png'))
    window = PixivTools()
    sys.exit(app.exec_())