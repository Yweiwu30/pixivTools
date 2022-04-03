# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pixivchecker.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PixivChecker(object):
    def setupUi(self, PixivChecker):
        if not PixivChecker.objectName():
            PixivChecker.setObjectName(u"PixivChecker")
        PixivChecker.resize(571, 611)
        self.centralwidget = QWidget(PixivChecker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 531, 151))
        self.PIDSubmit = QPushButton(self.groupBox)
        self.PIDSubmit.setObjectName(u"PIDSubmit")
        self.PIDSubmit.setGeometry(QRect(420, 110, 93, 28))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 491, 85))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPID = QLabel(self.layoutWidget)
        self.labelPID.setObjectName(u"labelPID")

        self.horizontalLayout.addWidget(self.labelPID)

        self.editPID = QLineEdit(self.layoutWidget)
        self.editPID.setObjectName(u"editPID")
        self.editPID.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.editPID)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.isMultiPage = QCheckBox(self.layoutWidget)
        self.isMultiPage.setObjectName(u"isMultiPage")

        self.verticalLayout.addWidget(self.isMultiPage)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPage = QLabel(self.layoutWidget)
        self.labelPage.setObjectName(u"labelPage")

        self.horizontalLayout_2.addWidget(self.labelPage)

        self.editPage = QSpinBox(self.layoutWidget)
        self.editPage.setObjectName(u"editPage")
        self.editPage.setMinimum(1)
        self.editPage.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.editPage)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelType = QLabel(self.layoutWidget)
        self.labelType.setObjectName(u"labelType")

        self.horizontalLayout_3.addWidget(self.labelType)

        self.pngButton = QRadioButton(self.layoutWidget)
        self.pngButton.setObjectName(u"pngButton")
        self.pngButton.setTabletTracking(False)
        self.pngButton.setAcceptDrops(False)
        self.pngButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pngButton)

        self.jpgButton = QRadioButton(self.layoutWidget)
        self.jpgButton.setObjectName(u"jpgButton")

        self.horizontalLayout_3.addWidget(self.jpgButton)

        self.gifButton = QRadioButton(self.layoutWidget)
        self.gifButton.setObjectName(u"gifButton")

        self.horizontalLayout_3.addWidget(self.gifButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.isMirror = QCheckBox(self.layoutWidget)
        self.isMirror.setObjectName(u"isMirror")
        self.isMirror.setChecked(True)

        self.verticalLayout_2.addWidget(self.isMirror)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(180, 560, 371, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.SavePicture = QPushButton(self.layoutWidget1)
        self.SavePicture.setObjectName(u"SavePicture")

        self.horizontalLayout_4.addWidget(self.SavePicture)

        self.ReloadPicture = QPushButton(self.layoutWidget1)
        self.ReloadPicture.setObjectName(u"ReloadPicture")

        self.horizontalLayout_4.addWidget(self.ReloadPicture)

        self.About = QPushButton(self.layoutWidget1)
        self.About.setObjectName(u"About")

        self.horizontalLayout_4.addWidget(self.About)

        self.PictureView = QLabel(self.centralwidget)
        self.PictureView.setObjectName(u"PictureView")
        self.PictureView.setGeometry(QRect(20, 180, 530, 375))
        self.PictureView.setMinimumSize(QSize(10, 10))
        self.PictureView.setMaximumSize(QSize(530, 375))
        self.PictureView.setAlignment(Qt.AlignCenter)
        PixivChecker.setCentralWidget(self.centralwidget)

        self.retranslateUi(PixivChecker)

        QMetaObject.connectSlotsByName(PixivChecker)
    # setupUi

    def retranslateUi(self, PixivChecker):
        PixivChecker.setWindowTitle(QCoreApplication.translate("PixivChecker", u"Pixiv\u56fe\u7247\u67e5\u770b", None))
#if QT_CONFIG(tooltip)
        PixivChecker.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        PixivChecker.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(QCoreApplication.translate("PixivChecker", u"\u56fe\u7247\u8bbe\u7f6e", None))
        self.PIDSubmit.setText(QCoreApplication.translate("PixivChecker", u"\u63d0\u4ea4", None))
        self.labelPID.setText(QCoreApplication.translate("PixivChecker", u"PID", None))
#if QT_CONFIG(whatsthis)
        self.editPID.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.editPID.setInputMask("")
        self.editPID.setText("")
        self.editPID.setPlaceholderText(QCoreApplication.translate("PixivChecker", u"\u5982\uff1a82775556", None))
        self.isMultiPage.setText(QCoreApplication.translate("PixivChecker", u"\u591a\u9875\u63d2\u753b", None))
        self.labelPage.setText(QCoreApplication.translate("PixivChecker", u"\u63d2\u753b\u9875\u6570", None))
        self.labelType.setText(QCoreApplication.translate("PixivChecker", u"\u56fe\u7247\u540e\u7f00\u540d", None))
        self.pngButton.setText(QCoreApplication.translate("PixivChecker", u"png", None))
        self.jpgButton.setText(QCoreApplication.translate("PixivChecker", u"jpg", None))
        self.gifButton.setText(QCoreApplication.translate("PixivChecker", u"gif\uff08\u52a8\u56fe\uff09", None))
        self.isMirror.setText(QCoreApplication.translate("PixivChecker", u"\u4f7f\u7528\u955c\u50cf\u57df\u540d\uff08\u63a8\u8350\uff09", None))
        self.SavePicture.setText(QCoreApplication.translate("PixivChecker", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.ReloadPicture.setText(QCoreApplication.translate("PixivChecker", u"\u5237\u65b0\u56fe\u7247", None))
        self.About.setText(QCoreApplication.translate("PixivChecker", u"\u5173\u4e8e..", None))
        self.PictureView.setText(QCoreApplication.translate("PixivChecker", u"\u56fe\u7247\u5c06\u5728\u8fd9\u91cc\u5c55\u793a...", None))
    # retranslateUi

