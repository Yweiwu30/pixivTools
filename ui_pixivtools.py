# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_pixivtools.ui'
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
        PixivTools.resize(577, 650)
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        PixivTools.setWindowIcon(icon)
        self.PixivTools_Tab = QTabWidget(PixivTools)
        self.PixivTools_Tab.setObjectName(u"PixivTools_Tab")
        self.PixivTools_Tab.setGeometry(QRect(10, 10, 561, 631))
        self.PIDCheck = QWidget()
        self.PIDCheck.setObjectName(u"PIDCheck")
        self.groupBox = QGroupBox(self.PIDCheck)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 531, 101))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 501, 71))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPID = QLabel(self.widget)
        self.labelPID.setObjectName(u"labelPID")

        self.horizontalLayout.addWidget(self.labelPID)

        self.editPID = QLineEdit(self.widget)
        self.editPID.setObjectName(u"editPID")

        self.horizontalLayout.addWidget(self.editPID)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.isMultiPage = QCheckBox(self.widget)
        self.isMultiPage.setObjectName(u"isMultiPage")

        self.horizontalLayout_3.addWidget(self.isMultiPage)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.editPage = QSpinBox(self.widget)
        self.editPage.setObjectName(u"editPage")

        self.horizontalLayout_2.addWidget(self.editPage)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.PIDSubmit = QPushButton(self.widget)
        self.PIDSubmit.setObjectName(u"PIDSubmit")

        self.horizontalLayout_3.addWidget(self.PIDSubmit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.PictureView = QLabel(self.PIDCheck)
        self.PictureView.setObjectName(u"PictureView")
        self.PictureView.setGeometry(QRect(10, 110, 531, 451))
        self.PictureView.setLayoutDirection(Qt.LeftToRight)
        self.PictureView.setAlignment(Qt.AlignCenter)
        self.widget1 = QWidget(self.PIDCheck)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 560, 531, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ResetPicture = QPushButton(self.widget1)
        self.ResetPicture.setObjectName(u"ResetPicture")

        self.horizontalLayout_4.addWidget(self.ResetPicture)

        self.OpenPicture = QPushButton(self.widget1)
        self.OpenPicture.setObjectName(u"OpenPicture")

        self.horizontalLayout_4.addWidget(self.OpenPicture)

        self.SavePicture = QPushButton(self.widget1)
        self.SavePicture.setObjectName(u"SavePicture")

        self.horizontalLayout_4.addWidget(self.SavePicture)

        self.ReloadPicture = QPushButton(self.widget1)
        self.ReloadPicture.setObjectName(u"ReloadPicture")

        self.horizontalLayout_4.addWidget(self.ReloadPicture)

        self.PixivTools_Tab.addTab(self.PIDCheck, "")
        self.RandomPic = QWidget()
        self.RandomPic.setObjectName(u"RandomPic")
        self.groupBox_2 = QGroupBox(self.RandomPic)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 531, 131))
        self.widget2 = QWidget(self.groupBox_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 20, 501, 99))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.KeywordSearch = QLineEdit(self.widget2)
        self.KeywordSearch.setObjectName(u"KeywordSearch")

        self.horizontalLayout_6.addWidget(self.KeywordSearch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.TagSearch = QLineEdit(self.widget2)
        self.TagSearch.setObjectName(u"TagSearch")

        self.horizontalLayout_7.addWidget(self.TagSearch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.isNsfw = QCheckBox(self.widget2)
        self.isNsfw.setObjectName(u"isNsfw")

        self.horizontalLayout_5.addWidget(self.isNsfw)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.RandomButton = QPushButton(self.widget2)
        self.RandomButton.setObjectName(u"RandomButton")

        self.horizontalLayout_8.addWidget(self.RandomButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.PictureView_2 = QLabel(self.RandomPic)
        self.PictureView_2.setObjectName(u"PictureView_2")
        self.PictureView_2.setGeometry(QRect(230, 140, 311, 421))
        self.PictureView_2.setLayoutDirection(Qt.LeftToRight)
        self.PictureView_2.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.RandomPic)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 560, 531, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ResetPicture_R = QPushButton(self.layoutWidget)
        self.ResetPicture_R.setObjectName(u"ResetPicture_R")

        self.horizontalLayout_9.addWidget(self.ResetPicture_R)

        self.OpenPicture_R = QPushButton(self.layoutWidget)
        self.OpenPicture_R.setObjectName(u"OpenPicture_R")

        self.horizontalLayout_9.addWidget(self.OpenPicture_R)

        self.SavePicture_R = QPushButton(self.layoutWidget)
        self.SavePicture_R.setObjectName(u"SavePicture_R")

        self.horizontalLayout_9.addWidget(self.SavePicture_R)

        self.ReloadPicture_R = QPushButton(self.layoutWidget)
        self.ReloadPicture_R.setObjectName(u"ReloadPicture_R")

        self.horizontalLayout_9.addWidget(self.ReloadPicture_R)

        self.groupBox_5 = QGroupBox(self.RandomPic)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 150, 221, 241))
        self.widget3 = QWidget(self.groupBox_5)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 20, 201, 211))
        self.verticalLayout_6 = QVBoxLayout(self.widget3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label = QLabel(self.widget3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_15.addWidget(self.label)

        self.pid_r = QLineEdit(self.widget3)
        self.pid_r.setObjectName(u"pid_r")
        self.pid_r.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.pid_r)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_4 = QLabel(self.widget3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_17.addWidget(self.label_4)

        self.name = QLineEdit(self.widget3)
        self.name.setObjectName(u"name")
        self.name.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.name)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.widget3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.author = QLineEdit(self.widget3)
        self.author.setObjectName(u"author")
        self.author.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.author)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.widget3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_19.addWidget(self.label_14)

        self.tagShow = QLineEdit(self.widget3)
        self.tagShow.setObjectName(u"tagShow")
        self.tagShow.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.tagShow)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.widget3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.date = QLineEdit(self.widget3)
        self.date.setObjectName(u"date")
        self.date.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.date)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.isAI = QCheckBox(self.widget3)
        self.isAI.setObjectName(u"isAI")
        self.isAI.setCheckable(False)

        self.verticalLayout_6.addWidget(self.isAI)

        self.label_12 = QLabel(self.RandomPic)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 390, 221, 51))
        self.PixivTools_Tab.addTab(self.RandomPic, "")
        self.DownloadLab = QWidget()
        self.DownloadLab.setObjectName(u"DownloadLab")
        self.layoutWidget_4 = QWidget(self.DownloadLab)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 10, 531, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.D_pid = QLineEdit(self.layoutWidget_4)
        self.D_pid.setObjectName(u"D_pid")

        self.horizontalLayout_10.addWidget(self.D_pid)

        self.Add = QPushButton(self.layoutWidget_4)
        self.Add.setObjectName(u"Add")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add.sizePolicy().hasHeightForWidth())
        self.Add.setSizePolicy(sizePolicy)
        self.Add.setMinimumSize(QSize(31, 29))
        self.Add.setMaximumSize(QSize(31, 29))

        self.horizontalLayout_10.addWidget(self.Add)

        self.pictureList = QListWidget(self.DownloadLab)
        self.pictureList.setObjectName(u"pictureList")
        self.pictureList.setGeometry(QRect(10, 50, 491, 441))
        self.downloadBar = QProgressBar(self.DownloadLab)
        self.downloadBar.setObjectName(u"downloadBar")
        self.downloadBar.setGeometry(QRect(10, 530, 541, 23))
        self.downloadBar.setValue(0)
        self.Download = QPushButton(self.DownloadLab)
        self.Download.setObjectName(u"Download")
        self.Download.setGeometry(QRect(450, 560, 93, 29))
        self.downloadInfo = QLineEdit(self.DownloadLab)
        self.downloadInfo.setObjectName(u"downloadInfo")
        self.downloadInfo.setGeometry(QRect(10, 500, 531, 24))
        self.downloadInfo.setReadOnly(True)
        self.widget4 = QWidget(self.DownloadLab)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(510, 50, 31, 67))
        self.verticalLayout_3 = QVBoxLayout(self.widget4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Delete = QPushButton(self.widget4)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setMaximumSize(QSize(29, 29))

        self.verticalLayout_3.addWidget(self.Delete)

        self.Clean = QPushButton(self.widget4)
        self.Clean.setObjectName(u"Clean")
        self.Clean.setMaximumSize(QSize(29, 29))

        self.verticalLayout_3.addWidget(self.Clean)

        self.PixivTools_Tab.addTab(self.DownloadLab, "")
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.groupBox_3 = QGroupBox(self.Setting)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(11, 11, 529, 121))
        self.widget5 = QWidget(self.groupBox_3)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(20, 20, 501, 91))
        self.verticalLayout_4 = QVBoxLayout(self.widget5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.widget5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.pngButton = QRadioButton(self.widget5)
        self.pngButton.setObjectName(u"pngButton")
        self.pngButton.setChecked(True)
        self.pngButton.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.pngButton)

        self.jpgButton = QRadioButton(self.widget5)
        self.jpgButton.setObjectName(u"jpgButton")

        self.horizontalLayout_11.addWidget(self.jpgButton)

        self.gifButton = QRadioButton(self.widget5)
        self.gifButton.setObjectName(u"gifButton")

        self.horizontalLayout_11.addWidget(self.gifButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.isMirror = QCheckBox(self.widget5)
        self.isMirror.setObjectName(u"isMirror")
        self.isMirror.setChecked(True)

        self.verticalLayout_4.addWidget(self.isMirror)

        self.isRemember = QCheckBox(self.widget5)
        self.isRemember.setObjectName(u"isRemember")

        self.verticalLayout_4.addWidget(self.isRemember)

        self.groupBox_4 = QGroupBox(self.Setting)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 140, 531, 131))
        self.widget6 = QWidget(self.groupBox_4)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(20, 30, 501, 92))
        self.verticalLayout_5 = QVBoxLayout(self.widget6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.widget6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.D_png = QRadioButton(self.widget6)
        self.D_png.setObjectName(u"D_png")
        self.D_png.setChecked(True)
        self.D_png.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.D_png)

        self.D_jpg = QRadioButton(self.widget6)
        self.D_jpg.setObjectName(u"D_jpg")

        self.horizontalLayout_13.addWidget(self.D_jpg)

        self.D_gif = QRadioButton(self.widget6)
        self.D_gif.setObjectName(u"D_gif")

        self.horizontalLayout_13.addWidget(self.D_gif)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.AutoFolder = QCheckBox(self.widget6)
        self.AutoFolder.setObjectName(u"AutoFolder")
        self.AutoFolder.setChecked(True)

        self.verticalLayout_5.addWidget(self.AutoFolder)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(self.widget6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.FolderNameEdit = QLineEdit(self.widget6)
        self.FolderNameEdit.setObjectName(u"FolderNameEdit")

        self.horizontalLayout_14.addWidget(self.FolderNameEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.PixivTools_Tab.addTab(self.Setting, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.About = QLabel(self.about)
        self.About.setObjectName(u"About")
        self.About.setGeometry(QRect(10, 10, 541, 581))
        self.About.setAlignment(Qt.AlignCenter)
        self.PixivTools_Tab.addTab(self.about, "")

        self.retranslateUi(PixivTools)

        self.PixivTools_Tab.setCurrentIndex(0)
        self.PIDSubmit.setDefault(True)
        self.RandomButton.setDefault(True)
        self.Add.setDefault(True)


        QMetaObject.connectSlotsByName(PixivTools)
    # setupUi

    def retranslateUi(self, PixivTools):
        PixivTools.setWindowTitle(QCoreApplication.translate("PixivTools", u"Pixiv\u5de5\u5177\u7bb1", None))
        self.groupBox.setTitle(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u8bbe\u7f6e", None))
        self.labelPID.setText(QCoreApplication.translate("PixivTools", u"PID", None))
        self.editPID.setText("")
        self.editPID.setPlaceholderText(QCoreApplication.translate("PixivTools", u"\u5982\uff1a82775556", None))
        self.isMultiPage.setText(QCoreApplication.translate("PixivTools", u"\u591a\u9875\u63d2\u753b", None))
        self.label_2.setText(QCoreApplication.translate("PixivTools", u"\u63d2\u753b\u9875\u6570", None))
        self.PIDSubmit.setText(QCoreApplication.translate("PixivTools", u"\u63d0\u4ea4", None))
        self.PictureView.setText(QCoreApplication.translate("PixivTools", u"TextLabel", None))
        self.ResetPicture.setText(QCoreApplication.translate("PixivTools", u"\u91cd\u7f6e\u56fe\u7247", None))
        self.OpenPicture.setText(QCoreApplication.translate("PixivTools", u"\u6253\u5f00\u56fe\u7247", None))
        self.SavePicture.setText(QCoreApplication.translate("PixivTools", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.ReloadPicture.setText(QCoreApplication.translate("PixivTools", u"\u5237\u65b0\u56fe\u7247", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.PIDCheck), QCoreApplication.translate("PixivTools", u"PID\u67e5\u56fe", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PixivTools", u"\u8bbe\u5b9a", None))
        self.label_5.setText(QCoreApplication.translate("PixivTools", u"\u5173\u952e\u8bcd\u641c\u7d22", None))
        self.KeywordSearch.setText("")
        self.KeywordSearch.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("PixivTools", u"\u6807\u7b7e", None))
        self.TagSearch.setText("")
        self.TagSearch.setPlaceholderText(QCoreApplication.translate("PixivTools", u"\u4f7f\u7528\u9017\u53f7\u5206\u9694\u591a\u4e2a\u6807\u7b7e\uff0c\u6700\u591a10\u4e2a", None))
        self.isNsfw.setText(QCoreApplication.translate("PixivTools", u"R-18", None))
        self.RandomButton.setText(QCoreApplication.translate("PixivTools", u"\u78b0\u78b0\u8fd0\u6c14", None))
        self.PictureView_2.setText(QCoreApplication.translate("PixivTools", u"TextLabel", None))
        self.ResetPicture_R.setText(QCoreApplication.translate("PixivTools", u"\u91cd\u7f6e\u56fe\u7247", None))
        self.OpenPicture_R.setText(QCoreApplication.translate("PixivTools", u"\u6253\u5f00\u56fe\u7247", None))
        self.SavePicture_R.setText(QCoreApplication.translate("PixivTools", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.ReloadPicture_R.setText(QCoreApplication.translate("PixivTools", u"\u5237\u65b0\u56fe\u7247", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PixivTools", u"\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("PixivTools", u"PID", None))
        self.label_4.setText(QCoreApplication.translate("PixivTools", u"\u6807\u9898", None))
        self.label_13.setText(QCoreApplication.translate("PixivTools", u"\u4f5c\u8005", None))
        self.label_14.setText(QCoreApplication.translate("PixivTools", u"\u6807\u7b7e", None))
        self.label_15.setText(QCoreApplication.translate("PixivTools", u"\u4e0a\u4f20\u65e5\u671f", None))
        self.isAI.setText(QCoreApplication.translate("PixivTools", u"AI\u751f\u6210\uff1f", None))
        self.label_12.setText(QCoreApplication.translate("PixivTools", u"Tips: \u5f53\u968f\u673a\u7684\u56fe\u662f\u56fe\u96c6\u65f6\uff0c\n"
"\u53f3\u4fa7\u9884\u89c8\u53ea\u4f1a\u5c55\u793a\u5176\u4e2d\u4e00\u5f20", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.RandomPic), QCoreApplication.translate("PixivTools", u"\u968f\u673a\u56fe", None))
        self.label_7.setText(QCoreApplication.translate("PixivTools", u"PID", None))
        self.D_pid.setText("")
        self.D_pid.setPlaceholderText(QCoreApplication.translate("PixivTools", u"\u5982\uff1a82775556", None))
        self.Add.setText(QCoreApplication.translate("PixivTools", u"+", None))
        self.Download.setText(QCoreApplication.translate("PixivTools", u"\u4e0b\u8f7d", None))
        self.Delete.setText(QCoreApplication.translate("PixivTools", u"-", None))
        self.Clean.setText(QCoreApplication.translate("PixivTools", u"X", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.DownloadLab), QCoreApplication.translate("PixivTools", u"\u6279\u91cf\u4e0b\u8f7d", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PixivTools", u"PID\u67e5\u56fe", None))
        self.label_8.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u540e\u7f00\u540d", None))
        self.pngButton.setText(QCoreApplication.translate("PixivTools", u"png", None))
        self.jpgButton.setText(QCoreApplication.translate("PixivTools", u"jpeg", None))
        self.gifButton.setText(QCoreApplication.translate("PixivTools", u"gif", None))
        self.isMirror.setText(QCoreApplication.translate("PixivTools", u"\u4f7f\u7528\u955c\u50cf\u57df\u540d\uff08\u63a8\u8350\uff09", None))
        self.isRemember.setText(QCoreApplication.translate("PixivTools", u"\u8bb0\u5f55\u56fe\u7247\u67e5\u8be2\u8bb0\u5f55", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PixivTools", u"\u6279\u91cf\u4e0b\u8f7d", None))
        self.label_10.setText(QCoreApplication.translate("PixivTools", u"\u56fe\u7247\u683c\u5f0f", None))
        self.D_png.setText(QCoreApplication.translate("PixivTools", u"png", None))
        self.D_jpg.setText(QCoreApplication.translate("PixivTools", u"jpeg", None))
        self.D_gif.setText(QCoreApplication.translate("PixivTools", u"gif", None))
        self.AutoFolder.setText(QCoreApplication.translate("PixivTools", u"\u81ea\u52a8\u5efa\u7acb\u6587\u4ef6\u5939", None))
        self.label_11.setText(QCoreApplication.translate("PixivTools", u"\u6587\u4ef6\u5939\u540d\u79f0", None))
        self.FolderNameEdit.setText(QCoreApplication.translate("PixivTools", u"Pixiv Download", None))
        self.FolderNameEdit.setPlaceholderText("")
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.Setting), QCoreApplication.translate("PixivTools", u"\u8bbe\u7f6e", None))
        self.About.setText(QCoreApplication.translate("PixivTools", u"TextLabel", None))
        self.PixivTools_Tab.setTabText(self.PixivTools_Tab.indexOf(self.about), QCoreApplication.translate("PixivTools", u"\u5173\u4e8e", None))
    # retranslateUi

