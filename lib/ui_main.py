# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainYMMESs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(786, 611)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u"icon/baseline_drive_file_move_outline_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/epsp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        icon2 = QIcon()
        icon2.addFile(u"icon/baseline_file_open_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_2.setIcon(icon2)
        self.actionprofile = QAction(MainWindow)
        self.actionprofile.setObjectName(u"actionprofile")
        self.actionprofile.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u"icon/baseline_fingerprint_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionprofile.setIcon(icon3)
        self.actionProcess = QAction(MainWindow)
        self.actionProcess.setObjectName(u"actionProcess")
        self.actionProcess.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u"icon/baseline_memory_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionProcess.setIcon(icon4)
        self.actionNetwok = QAction(MainWindow)
        self.actionNetwok.setObjectName(u"actionNetwok")
        self.actionNetwok.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u"icon/baseline_travel_explore_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNetwok.setIcon(icon5)
        self.actionFiles = QAction(MainWindow)
        self.actionFiles.setObjectName(u"actionFiles")
        self.actionFiles.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u"icon/baseline_sim_card_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFiles.setIcon(icon6)
        self.actionExport_2 = QAction(MainWindow)
        self.actionExport_2.setObjectName(u"actionExport_2")
        self.actionExport_2.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u"icon/baseline_exit_to_app_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport_2.setIcon(icon7)
        self.actionAlertConfig = QAction(MainWindow)
        self.actionAlertConfig.setObjectName(u"actionAlertConfig")
        icon8 = QIcon()
        icon8.addFile(u"icon/baseline_notification_important_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAlertConfig.setIcon(icon8)
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionSearch.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u"icon/baseline_search_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearch.setIcon(icon9)
        self.actionprocess_cmd = QAction(MainWindow)
        self.actionprocess_cmd.setObjectName(u"actionprocess_cmd")
        self.actionprocess_cmd.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u"icon/baseline_terminal_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionprocess_cmd.setIcon(icon10)
        self.actionprocess_tree = QAction(MainWindow)
        self.actionprocess_tree.setObjectName(u"actionprocess_tree")
        self.actionprocess_tree.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(u"icon/baseline_account_tree_black_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionprocess_tree.setIcon(icon11)
        self.actiongdxg = QAction(MainWindow)
        self.actiongdxg.setObjectName(u"actiongdxg")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainStack = QStackedWidget(self.centralwidget)
        self.MainStack.setObjectName(u"MainStack")
        self.Process = QWidget()
        self.Process.setObjectName(u"Process")
        self.gridLayout = QGridLayout(self.Process)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.Process)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAnimated(False)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.MainStack.addWidget(self.Process)
        self.TreeProcess = QWidget()
        self.TreeProcess.setObjectName(u"TreeProcess")
        self.gridLayout_2 = QGridLayout(self.TreeProcess)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeWidget_2 = QTreeWidget(self.TreeProcess)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(__qtreewidgetitem)
        self.treeWidget_2.setObjectName(u"treeWidget_2")

        self.gridLayout_2.addWidget(self.treeWidget_2, 0, 0, 1, 1)

        self.MainStack.addWidget(self.TreeProcess)
        self.Cmdline = QWidget()
        self.Cmdline.setObjectName(u"Cmdline")
        self.gridLayout_3 = QGridLayout(self.Cmdline)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.treeWidget_3 = QTreeWidget(self.Cmdline)
        QTreeWidgetItem(self.treeWidget_3)
        QTreeWidgetItem(self.treeWidget_3)
        QTreeWidgetItem(self.treeWidget_3)
        self.treeWidget_3.setObjectName(u"treeWidget_3")

        self.gridLayout_3.addWidget(self.treeWidget_3, 0, 0, 1, 1)

        self.MainStack.addWidget(self.Cmdline)
        self.Network = QWidget()
        self.Network.setObjectName(u"Network")
        self.gridLayout_4 = QGridLayout(self.Network)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.treeWidget_4 = QTreeWidget(self.Network)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeWidget_4.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget_4.setObjectName(u"treeWidget_4")

        self.gridLayout_4.addWidget(self.treeWidget_4, 0, 0, 1, 1)

        self.MainStack.addWidget(self.Network)
        self.Files = QWidget()
        self.Files.setObjectName(u"Files")
        self.gridLayout_5 = QGridLayout(self.Files)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.treeWidget_5 = QTreeWidget(self.Files)
        icon12 = QIcon()
        icon12.addFile(u"Fileicon/folder-green.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13 = QIcon()
        icon13.addFile(u"Fileicon/application-video.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14 = QIcon()
        icon14.addFile(u"Fileicon/application-octet-stream.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15 = QIcon()
        icon15.addFile(u"Fileicon/application-images.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16 = QIcon()
        icon16.addFile(u"Fileicon/application-pdf.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17 = QIcon()
        icon17.addFile(u"Fileicon/application-table.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon18 = QIcon()
        icon18.addFile(u"Fileicon/application-archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon19 = QIcon()
        icon19.addFile(u"Fileicon/application-audio.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem2.setIcon(0, icon12);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3.setIcon(0, icon12);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4.setIcon(0, icon12);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5.setIcon(0, icon13);
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem6.setIcon(0, icon14);
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem7.setIcon(0, icon15);
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem8.setIcon(0, icon12);
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem9.setIcon(0, icon12);
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10.setIcon(0, icon12);
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem11.setIcon(0, icon16);
        __qtreewidgetitem12 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem12.setIcon(0, icon12);
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13.setIcon(0, icon12);
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem13)
        __qtreewidgetitem14.setIcon(0, icon15);
        __qtreewidgetitem15 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem15.setIcon(0, icon15);
        __qtreewidgetitem16 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem16.setIcon(0, icon12);
        QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem17 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem17.setIcon(0, icon17);
        __qtreewidgetitem18 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem18.setIcon(0, icon18);
        __qtreewidgetitem19 = QTreeWidgetItem(self.treeWidget_5)
        __qtreewidgetitem19.setIcon(0, icon12);
        __qtreewidgetitem20 = QTreeWidgetItem(__qtreewidgetitem19)
        __qtreewidgetitem20.setIcon(0, icon12);
        __qtreewidgetitem21 = QTreeWidgetItem(__qtreewidgetitem20)
        __qtreewidgetitem21.setIcon(0, icon19);
        self.treeWidget_5.setObjectName(u"treeWidget_5")

        self.gridLayout_5.addWidget(self.treeWidget_5, 0, 0, 1, 1)

        self.MainStack.addWidget(self.Files)

        self.verticalLayout.addWidget(self.MainStack)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 786, 24))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuOpen = QMenu(self.menubar)
        self.menuOpen.setObjectName(u"menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menuEdit.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionExport)
        self.menuEdit.addAction(self.actionClose)
        self.toolBar.addAction(self.actionOpen_2)
        self.toolBar.addAction(self.actionprofile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionProcess)
        self.toolBar.addAction(self.actionprocess_tree)
        self.toolBar.addAction(self.actionprocess_cmd)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNetwok)
        self.toolBar.addAction(self.actionFiles)
        self.toolBar_2.addAction(self.actionSearch)
        self.toolBar_2.addAction(self.actionExport_2)
        self.toolBar_2.addAction(self.actionAlertConfig)

        self.retranslateUi(MainWindow)

        self.MainStack.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionprofile.setText(QCoreApplication.translate("MainWindow", u"profile", None))
        self.actionProcess.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.actionNetwok.setText(QCoreApplication.translate("MainWindow", u"Netwok", None))
        self.actionFiles.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.actionExport_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionAlertConfig.setText(QCoreApplication.translate("MainWindow", u"AlertConfig", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.actionprocess_cmd.setText(QCoreApplication.translate("MainWindow", u"process cmd", None))
        self.actionprocess_tree.setText(QCoreApplication.translate("MainWindow", u"process tree", None))
        self.actiongdxg.setText(QCoreApplication.translate("MainWindow", u"gdxg", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"File output", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"ExitTime", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"CreateTime", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Wow64", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"SessionId", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Handles", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Threads", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"PPID", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"PID", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(9, QCoreApplication.translate("MainWindow", u"Disabled", None));
        ___qtreewidgetitem1.setText(8, QCoreApplication.translate("MainWindow", u"2020-03-21 10:01:21.000000", None));
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u" 2020-03-21 10:01:19.000000", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"False", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"120", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"10", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"spoolsv.exe", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"1248", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"964", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem2 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem2.setText(8, QCoreApplication.translate("MainWindow", u"ExitTime", None));
        ___qtreewidgetitem2.setText(7, QCoreApplication.translate("MainWindow", u"CreateTime", None));
        ___qtreewidgetitem2.setText(6, QCoreApplication.translate("MainWindow", u"Wow64", None));
        ___qtreewidgetitem2.setText(5, QCoreApplication.translate("MainWindow", u"SessionId", None));
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"Handles", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Threads", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"PPID", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"PID", None));

        __sortingEnabled1 = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem3 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem3.setText(8, QCoreApplication.translate("MainWindow", u"N/A", None));
        ___qtreewidgetitem3.setText(7, QCoreApplication.translate("MainWindow", u"N/A", None));
        ___qtreewidgetitem3.setText(6, QCoreApplication.translate("MainWindow", u"False", None));
        ___qtreewidgetitem3.setText(5, QCoreApplication.translate("MainWindow", u"N/A", None));
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"256", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"50", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"System", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"0", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"4", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(8, QCoreApplication.translate("MainWindow", u"N/A", None));
        ___qtreewidgetitem4.setText(7, QCoreApplication.translate("MainWindow", u"2020-03-21 07:59:05.000000", None));
        ___qtreewidgetitem4.setText(6, QCoreApplication.translate("MainWindow", u"False", None));
        ___qtreewidgetitem4.setText(5, QCoreApplication.translate("MainWindow", u"N/A", None));
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", u"16", None));
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"3", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"smss.exe", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"4", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"400", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled1)

        ___qtreewidgetitem5 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"Args", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"Process", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"PID", None));

        __sortingEnabled2 = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        ___qtreewidgetitem6 = self.treeWidget_3.topLevelItem(0)
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("MainWindow", u"Required memory at 0x10 is not valid (process exited?)", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"System", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"4", None));
        ___qtreewidgetitem7 = self.treeWidget_3.topLevelItem(1)
        ___qtreewidgetitem7.setText(2, QCoreApplication.translate("MainWindow", u"\\SystemRoot\\System32\\smss.exe", None));
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"smss.exe", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"400", None));
        ___qtreewidgetitem8 = self.treeWidget_3.topLevelItem(2)
        ___qtreewidgetitem8.setText(2, QCoreApplication.translate("MainWindow", u"C:\\WINDOWS\\system32\\csrss.exe ObjectDirectory=\\Windows SharedSection=1024,3072,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ProfileControl=Off MaxRequestThreads=16\n"
"", None));
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("MainWindow", u"csrss.exe", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"456", None));
        self.treeWidget_3.setSortingEnabled(__sortingEnabled2)

        ___qtreewidgetitem9 = self.treeWidget_5.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));

        __sortingEnabled3 = self.treeWidget_5.isSortingEnabled()
        self.treeWidget_5.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.treeWidget_5.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem11.child(2)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem16 = self.treeWidget_5.topLevelItem(1)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem18.child(0)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem20 = self.treeWidget_5.topLevelItem(2)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem20.child(0)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem21.child(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem23 = self.treeWidget_5.topLevelItem(3)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem24 = self.treeWidget_5.topLevelItem(4)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem24.child(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem26 = self.treeWidget_5.topLevelItem(5)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem27 = self.treeWidget_5.topLevelItem(6)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem28 = self.treeWidget_5.topLevelItem(7)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem28.child(0)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem29.child(0)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        self.treeWidget_5.setSortingEnabled(__sortingEnabled3)

        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file ", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"icons", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

