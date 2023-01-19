# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pixivtools-set.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PixivTools(object):
    def setupUi(self, PixivTools):
        if not PixivTools.objectName():
            PixivTools.setObjectName(u"PixivTools")
        PixivTools.resize(580, 650)
        self.centralwidget = QWidget(PixivTools)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PixivTools_Tab = QTabWidget(self.centralwidget)
        self.PixivTools_Tab.setObjectName(u"PixivTools_Tab")
        self.PixivTools_Tab.setGeometry(QRect(10, 10, 561, 611))
        self.PIDCheck = QWidget()
        self.PIDCheck.setObjectName(u"PIDCheck")
        self.groupBox = QGroupBox(self.PIDCheck)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 531, 111))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(18, 29, 491, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelPID = QLabel(self.layoutWidget)
        self.labelPID.setObjectName(u"labelPID")

        self.horizontalLayout.addWidget(self.labelPID)

        self.editPID = QLineEdit(self.layoutWidget)
        self.editPID.setObjectName(u"editPID")
        self.editPID.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.editPID)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 60, 491, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.isMultiPage = QCheckBox(self.layoutWidget1)
        self.isMultiPage.setObjectName(u"isMultiPage")

        self.horizontalLayout_5.addWidget(self.isMultiPage)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPage = QLabel(self.layoutWidget1)
        self.labelPage.setObjectName(u"labelPage")

        self.horizontalLayout_2.addWidget(self.labelPage)

        self.editPage = QSpinBox(self.layoutWidget1)
        self.editPage.setObjectName(u"editPage")
        self.editPage.setMinimum(1)
        self.editPage.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.editPage)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.PIDSubmit = QPushButton(self.layoutWidget1)
        self.PIDSubmit.setObjectName(u"PIDSubmit")

        self.horizontalLayout_5.addWidget(self.PIDSubmit)

        self.PictureView = QLabel(self.PIDCheck)
        self.PictureView.setObjectName(u"PictureView")
        self.PictureView.setGeometry(QRect(10, 125, 530, 420))
        self.PictureView.setMinimumSize(QSize(10, 10))
        self.PictureView.setMaximumSize(QSize(530, 420))
        self.PictureView.setAlignment(Qt.AlignCenter)
        self.layoutWidget2 = QWidget(self.PIDCheck)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(90, 550, 461, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ResetPicture = QPushButton(self.layoutWidget2)
        self.ResetPicture.setObjectName(u"ResetPicture")

        self.horizontalLayout_4.addWidget(self.ResetPicture)

        self.OpenPicture = QPushButton(self.layoutWidget2)
        self.OpenPicture.setObjectName(u"OpenPicture")

        self.horizontalLayout_4.addWidget(self.OpenPicture)

        self.SavePicture = QPushButton(self.layoutWidget2)
        self.SavePicture.setObjectName(u"SavePicture")

        self.horizontalLayout_4.addWidget(self.SavePicture)

        self.ReloadPicture = QPushButton(self.layoutWidget2)
        self.ReloadPicture.setObjectName(u"ReloadPicture")

        self.horizontalLayout_4.addWidget(self.ReloadPicture)

        self.PixivTools_Tab.addTab(self.PIDCheck, "")
        self.RandomRank = QWidget()
        self.RandomRank.setObjectName(u"RandomRank")
        self.PictureView_2 = QLabel(self.RandomRank)
        self.PictureView_2.setObjectName(u"PictureView_2")
        self.PictureView_2.setGeometry(QRect(20, 224, 510, 300))
        self.PictureView_2.setMinimumSize(QSize(10, 10))
        self.PictureView_2.setMaximumSize(QSize(530, 375))
        self.PictureView_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.RandomRank)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(19, 19, 511, 61))
        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 491, 30))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Daily = QRadioButton(self.layoutWidget3)
        self.Daily.setObjectName(u"Daily")
        self.Daily.setChecked(True)

        self.horizontalLayout_6.addWidget(self.Daily)

        self.Weekly = QRadioButton(self.layoutWidget3)
        self.Weekly.setObjectName(u"Weekly")

        self.horizontalLayout_6.addWidget(self.Weekly)

        self.Monthly = QRadioButton(self.layoutWidget3)
        self.Monthly.setObjectName(u"Monthly")

        self.horizontalLayout_6.addWidget(self.Monthly)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.RandomButton = QPushButton(self.layoutWidget3)
        self.RandomButton.setObjectName(u"RandomButton")

        self.horizontalLayout_7.addWidget(self.RandomButton)

        self.groupBox_3 = QGroupBox(self.RandomRank)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 90, 511, 121))
        self.layoutWidget4 = QWidget(self.groupBox_3)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(21, 20, 471, 91))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.name_l = QLabel(self.layoutWidget4)
        self.name_l.setObjectName(u"name_l")
        self.name_l.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.name_l)

        self.name = QLineEdit(self.layoutWidget4)
        self.name.setObjectName(u"name")
        self.name.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.name)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.date_l = QLabel(self.layoutWidget4)
        self.date_l.setObjectName(u"date_l")
        self.date_l.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.date_l)

        self.date = QLineEdit(self.layoutWidget4)
        self.date.setObjectName(u"date")
        self.date.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.date)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pid_l = QLabel(self.layoutWidget4)
        self.pid_l.setObjectName(u"pid_l")
        self.pid_l.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.pid_l)

        self.pid_r = QLineEdit(self.layoutWidget4)
        self.pid_r.setObjectName(u"pid_r")
        self.pid_r.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.pid_r)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tag_l = QLabel(self.layoutWidget4)
        self.tag_l.setObjectName(u"tag_l")

        self.horizontalLayout_15.addWidget(self.tag_l)

        self.tag = QLineEdit(self.layoutWidget4)
        self.tag.setObjectName(u"tag")
        self.tag.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.tag)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.layoutWidget_3 = QWidget(self.RandomRank)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(180, 550, 371, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ResetPicture_R = QPushButton(self.layoutWidget_3)
        self.ResetPicture_R.setObjectName(u"ResetPicture_R")

        self.horizontalLayout_8.addWidget(self.ResetPicture_R)

        self.SavePicture_R = QPushButton(self.layoutWidget_3)
        self.SavePicture_R.setObjectName(u"SavePicture_R")

        self.horizontalLayout_8.addWidget(self.SavePicture_R)

        self.ReloadPicture_R = QPushButton(self.layoutWidget_3)
        self.ReloadPicture_R.setObjectName(u"ReloadPicture_R")

        self.horizontalLayout_8.addWidget(self.ReloadPicture_R)

        self.PixivTools_Tab.addTab(self.RandomRank, "")
        self.DownloadLab = QWidget()
        self.DownloadLab.setObjectName(u"DownloadLab")
        self.Download = QPushButton(self.DownloadLab)
        self.Download.setObjectName(u"Download")
        self.Download.setGeometry(QRect(450, 550, 93, 28))
        self.pictureList = QListWidget(self.DownloadLab)
        self.pictureList.setObjectName(u"pictureList")
        self.pictureList.setGeometry(QRect(20, 50, 481, 441))
        self.Clean = QPushButton(self.DownloadLab)
        self.Clean.setObjectName(u"Clean")
        self.Clean.setGeometry(QRect(510, 80, 28, 28))
        self.Clean.setMinimumSize(QSize(28, 28))
        self.Clean.setMaximumSize(QSize(28, 28))
        self.Delete = QPushButton(self.DownloadLab)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setGeometry(QRect(510, 50, 28, 28))
        self.Delete.setMinimumSize(QSize(28, 28))
        self.Delete.setMaximumSize(QSize(28, 28))
        self.layoutWidget5 = QWidget(self.DownloadLab)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 10, 521, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.D_pid = QLineEdit(self.layoutWidget5)
        self.D_pid.setObjectName(u"D_pid")

        self.horizontalLayout_11.addWidget(self.D_pid)

        self.Add = QPushButton(self.layoutWidget5)
        self.Add.setObjectName(u"Add")
        self.Add.setMinimumSize(QSize(28, 28))
        self.Add.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_11.addWidget(self.Add)

        self.downloadBar = QProgressBar(self.DownloadLab)
        self.downloadBar.setObjectName(u"downloadBar")
        self.downloadBar.setGeometry(QRect(20, 510, 521, 23))
        self.downloadBar.setValue(0)
        self.PixivTools_Tab.addTab(self.DownloadLab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 260, 511, 101))
        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 30, 91, 19))
        self.checkBox.setChecked(True)
        self.layoutWidget6 = QWidget(self.groupBox_5)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 60, 471, 21))
        self.horizontalLayout_18 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_18.addWidget(self.label_5)

        self.radioButton = QRadioButton(self.layoutWidget6)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_18.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget6)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.horizontalLayout_18.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.layoutWidget6)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_18.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.layoutWidget6)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_18.addWidget(self.radioButton_4)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(432, 540, 111, 28))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 540, 101, 28))
        #self.groupBox_6 = QGroupBox(self.tab)
        #self.groupBox_6.setObjectName(u"groupBox_6")
        #self.groupBox_6.setGeometry(QRect(20, 370, 511, 80))
        #self.checkBox_2 = QCheckBox(self.groupBox_6)
        #self.checkBox_2.setObjectName(u"checkBox_2")
        #self.checkBox_2.setGeometry(QRect(20, 40, 161, 19))
        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(20, 20, 511, 121))
        self.layoutWidget_4 = QWidget(self.groupBox_8)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 30, 311, 75))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelType = QLabel(self.layoutWidget_4)
        self.labelType.setObjectName(u"labelType")

        self.horizontalLayout_3.addWidget(self.labelType)

        self.pngButton = QRadioButton(self.layoutWidget_4)
        self.pngButton.setObjectName(u"pngButton")
        self.pngButton.setTabletTracking(False)
        self.pngButton.setAcceptDrops(False)
        self.pngButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pngButton)

        self.jpgButton = QRadioButton(self.layoutWidget_4)
        self.jpgButton.setObjectName(u"jpgButton")

        self.horizontalLayout_3.addWidget(self.jpgButton)

        self.gifButton = QRadioButton(self.layoutWidget_4)
        self.gifButton.setObjectName(u"gifButton")

        self.horizontalLayout_3.addWidget(self.gifButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.isMirror = QCheckBox(self.layoutWidget_4)
        self.isMirror.setObjectName(u"isMirror")
        self.isMirror.setChecked(True)

        self.verticalLayout_2.addWidget(self.isMirror)

        self.isRemember = QCheckBox(self.layoutWidget_4)
        self.isRemember.setObjectName(u"isRemember")
        self.isRemember.setChecked(True)

        self.verticalLayout_2.addWidget(self.isRemember)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 150, 511, 101))
        self.layoutWidget7 = QWidget(self.groupBox_4)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(20, 30, 424, 54))
        self.verticalLayout = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.AutoFolder = QCheckBox(self.layoutWidget7)
        self.AutoFolder.setObjectName(u"AutoFolder")
        self.AutoFolder.setChecked(True)

        self.horizontalLayout_12.addWidget(self.AutoFolder)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.layoutWidget7)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)

        self.D_png = QRadioButton(self.layoutWidget7)
        self.D_png.setObjectName(u"D_png")
        self.D_png.setChecked(True)

        self.horizontalLayout_12.addWidget(self.D_png)

        self.D_jpg = QRadioButton(self.layoutWidget7)
        self.D_jpg.setObjectName(u"D_jpg")

        self.horizontalLayout_12.addWidget(self.D_jpg)

        self.D_gif = QRadioButton(self.layoutWidget7)
        self.D_gif.setObjectName(u"D_gif")

        self.horizontalLayout_12.addWidget(self.D_gif)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_3 = QLabel(self.layoutWidget7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_17.addWidget(self.label_3)

        self.NamePid = QRadioButton(self.layoutWidget7)
        self.NamePid.setObjectName(u"NamePid")
        self.NamePid.setChecked(True)

        self.horizontalLayout_17.addWidget(self.NamePid)

        self.NameNo = QRadioButton(self.layoutWidget7)
        self.NameNo.setObjectName(u"NameNo")

        self.horizontalLayout_17.addWidget(self.NameNo)

        self.NameSelf = QRadioButton(self.layoutWidget7)
        self.NameSelf.setObjectName(u"NameSelf")

        self.horizontalLayout_17.addWidget(self.NameSelf)

        self.NameEdit = QLineEdit(self.layoutWidget7)
        self.NameEdit.setObjectName(u"NameEdit")
        self.NameEdit.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.NameEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.PixivTools_Tab.addTab(self.tab, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.About = QLabel(self.about)
        self.About.setObjectName(u"About")
        self.About.setGeometry(QRect(10, 10, 541, 561))
        self.About.setAlignment(Qt.AlignCenter)
        self.PixivTools_Tab.addTab(self.about, "")
        PixivTools.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(PixivTools)
        self.statusBar.setObjectName(u"statusBar")
        PixivTools.setStatusBar(self.statusBar)

        self.retranslateUi(PixivTools)

        self.PixivTools_Tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PixivTools)
    # setupUi

    def retranslateUi(self, PixivTools):
        PixivTools.setWindowTitle(QCoreApplication.translate("PixivTools", u"Pixiv\u5de5\u5177\u7bb1", None))
#if QT_CONFIG(tooltip)
        PixivTools.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        PixivTools.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.PixivTools_Tab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u8bbe\u7f6e", None))
        self.labelPID.setText(QCoreApplication.translate("PixivTools", u"PID", None))
#if QT_CONFIG(whatsthis)
        self.editPID.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.editPID.setInputMask("")
        self.editPID.setText("")
        self.editPID.setPlaceholderText(QCoreApplication.translate("PixivTools", u"\u5982\uff1a82775556", None))
        self.isMultiPage.setText(QCoreApplication.translate("PixivTools", u"\u591a\u9875\u63d2\u753b", None))
        self.labelPage.setText(QCoreApplication.translate("PixivTools", u"\u63d2\u753b\u9875\u6570", None))
        self.PIDSubmit.setText(QCoreApplication.translate("PixivTools", u"\u63d0\u4ea4", None))
        self.PictureView.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u5c06\u5728\u8fd9\u91cc\u5c55\u793a...", None))
        self.ResetPicture.setText(QCoreApplication.translate("PixivTools", u"\u91cd\u7f6e\u56fe\u7247", None))
        self.OpenPicture.setText(QCoreApplication.translate("PixivTools", u"\u6253\u5f00\u56fe\u7247", None))
        self.SavePicture.setText(QCoreApplication.translate("PixivTools", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.ReloadPicture.setText(QCoreApplication.translate("PixivTools", u"\u5237\u65b0\u56fe\u7247", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.PIDCheck), QCoreApplication.translate("PixivTools", u"PID\u67e5\u56fe", None))
        self.PictureView_2.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u5c06\u5728\u8fd9\u91cc\u5c55\u793a...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PixivTools", u"\u8bbe\u5b9a", None))
        self.Daily.setText(QCoreApplication.translate("PixivTools", u"\u65e5\u699c", None))
        self.Weekly.setText(QCoreApplication.translate("PixivTools", u"\u5468\u699c", None))
        self.Monthly.setText(QCoreApplication.translate("PixivTools", u"\u6708\u699c", None))
        self.RandomButton.setText(QCoreApplication.translate("PixivTools", u"\u78b0\u78b0\u8fd0\u6c14", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u4fe1\u606f", None))
        self.name_l.setText(QCoreApplication.translate("PixivTools", u"\u63d2\u56fe\u540d\u79f0: ", None))
        self.name.setText("")
        self.date_l.setText(QCoreApplication.translate("PixivTools", u"\u53d1\u5e03\u65e5\u671f: ", None))
        self.date.setText("")
        self.pid_l.setText(QCoreApplication.translate("PixivTools", u"Pixiv ID:", None))
        self.pid_r.setText("")
        self.tag_l.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u6807\u7b7e: ", None))
        self.tag.setText("")
        self.ResetPicture_R.setText(QCoreApplication.translate("PixivTools", u"\u91cd\u7f6e\u56fe\u7247", None))
        self.SavePicture_R.setText(QCoreApplication.translate("PixivTools", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.ReloadPicture_R.setText(QCoreApplication.translate("PixivTools", u"\u5237\u65b0\u56fe\u7247", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.RandomRank), QCoreApplication.translate("PixivTools", u"\u968f\u673a\u699c\u5355\u56fe", None))
#if QT_CONFIG(accessibility)
        self.DownloadLab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.Download.setText(QCoreApplication.translate("PixivTools", u"\u4e0b\u8f7d", None))
        self.Clean.setText(QCoreApplication.translate("PixivTools", u"X", None))
        self.Delete.setText(QCoreApplication.translate("PixivTools", u"-", None))
        self.label.setText(QCoreApplication.translate("PixivTools", u"PID", None))
        self.D_pid.setInputMask("")
        self.D_pid.setPlaceholderText(QCoreApplication.translate("PixivTools", u"\u6dfb\u52a0\u591a\u4e2apid\u7528\u7a7a\u683c\u5206\u9694", None))
        self.Add.setText(QCoreApplication.translate("PixivTools", u"+", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.DownloadLab), QCoreApplication.translate("PixivTools", u"\u6279\u91cf\u4e0b\u8f7d", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PixivTools", u"\u65e5\u5fd7", None))
        self.checkBox.setText(QCoreApplication.translate("PixivTools", u"\u8bb0\u5f55\u65e5\u5fd7", None))
        self.label_5.setText(QCoreApplication.translate("PixivTools", u"\u65e5\u5fd7\u7ea7\u522b", None))
        self.radioButton.setText(QCoreApplication.translate("PixivTools", u"Debug", None))
        self.radioButton_2.setText(QCoreApplication.translate("PixivTools", u"Info", None))
        self.radioButton_3.setText(QCoreApplication.translate("PixivTools", u"Warning", None))
        self.radioButton_4.setText(QCoreApplication.translate("PixivTools", u"Error", None))
        self.pushButton.setText(QCoreApplication.translate("PixivTools", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("PixivTools", u"\u91cd\u7f6e", None))
        #self.groupBox_6.setTitle(QCoreApplication.translate("PixivTools", u"\u5176\u4ed6", None))
        #self.checkBox_2.setText(QCoreApplication.translate("PixivTools", u"\u62a5\u9519\u65f6\u81ea\u52a8\u5173\u95ed\u8f6f\u4ef6", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("PixivTools", u"PID\u67e5\u56fe", None))
        self.labelType.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u540e\u7f00\u540d", None))
        self.pngButton.setText(QCoreApplication.translate("PixivTools", u"png", None))
        self.jpgButton.setText(QCoreApplication.translate("PixivTools", u"jpg", None))
        self.gifButton.setText(QCoreApplication.translate("PixivTools", u"gif       ", None))
        self.isMirror.setText(QCoreApplication.translate("PixivTools", u"\u4f7f\u7528\u955c\u50cf\u57df\u540d\uff08\u63a8\u8350\uff09", None))
        self.isRemember.setText(QCoreApplication.translate("PixivTools", u"\u8bb0\u5f55\u56fe\u7247\u67e5\u8be2\u8bb0\u5f55", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PixivTools", u"\u6279\u91cf\u4e0b\u8f7d", None))
        self.AutoFolder.setText(QCoreApplication.translate("PixivTools", u"\u81ea\u52a8\u5efa\u7acb\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u683c\u5f0f", None))
        self.D_png.setText(QCoreApplication.translate("PixivTools", u"png", None))
        self.D_jpg.setText(QCoreApplication.translate("PixivTools", u"jpg", None))
        self.D_gif.setText(QCoreApplication.translate("PixivTools", u"gif", None))
        self.label_3.setText(QCoreApplication.translate("PixivTools", u"\u6587\u4ef6\u540d", None))
        self.NamePid.setText(QCoreApplication.translate("PixivTools", u"pid", None))
        self.NameNo.setText(QCoreApplication.translate("PixivTools", u"No.", None))
        self.NameSelf.setText(QCoreApplication.translate("PixivTools", u"\u81ea\u5b9a\u4e49", None))
        self.NameEdit.setPlaceholderText("")
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.tab), QCoreApplication.translate("PixivTools", u"\u8bbe\u7f6e", None))
        self.About.setText(QCoreApplication.translate("PixivTools", u"\u5173\u4e8e\u672c\u8f6f\u4ef6...", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.about), QCoreApplication.translate("PixivTools", u"\u5173\u4e8e", None))
    # retranslateUi

