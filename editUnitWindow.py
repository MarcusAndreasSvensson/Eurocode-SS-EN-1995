# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editUnitWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editUnitWindow(object):
    def setupUi(self, editUnitWindow):
        editUnitWindow.setObjectName("editUnitWindow")
        editUnitWindow.resize(539, 485)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(editUnitWindow)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 531, 471))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_11)
        self.tabWidget.setObjectName("tabWidget")
        self.generalTab = QtWidgets.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.tabWidget.addTab(self.generalTab, "")
        self.sectionTab = QtWidgets.QWidget()
        self.sectionTab.setObjectName("sectionTab")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.sectionTab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 521, 421))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bothEndsCheckBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.bothEndsCheckBox_2.setObjectName("bothEndsCheckBox_2")
        self.horizontalLayout_2.addWidget(self.bothEndsCheckBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.endButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.endButton.setObjectName("endButton")
        self.horizontalLayout_2.addWidget(self.endButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView_2 = QtWidgets.QTreeView(self.verticalLayoutWidget_9)
        self.treeView_2.setObjectName("treeView_2")
        self.verticalLayout.addWidget(self.treeView_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.verticalLayoutWidget_9)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout_4.addWidget(self.openGLWidget)
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_9)
        self.listView.setObjectName("listView")
        self.verticalLayout_4.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.newButton.setObjectName("newButton")
        self.horizontalLayout_3.addWidget(self.newButton)
        self.modifyButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.modifyButton.setObjectName("modifyButton")
        self.horizontalLayout_3.addWidget(self.modifyButton)
        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_3.addWidget(self.deleteButton)
        self.importButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_3.addWidget(self.importButton)
        self.exportButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_3.addWidget(self.exportButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.sectionTab, "")
        self.endConditionsTab = QtWidgets.QWidget()
        self.endConditionsTab.setObjectName("endConditionsTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.endConditionsTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.eccLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.eccLabel.setObjectName("eccLabel")
        self.horizontalLayout_15.addWidget(self.eccLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_15.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_15.addWidget(self.pushButton_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.considerEccCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.considerEccCheckBox.setObjectName("considerEccCheckBox")
        self.verticalLayout_7.addWidget(self.considerEccCheckBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.bothEndsCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bothEndsCheckBox.setObjectName("bothEndsCheckBox")
        self.horizontalLayout_14.addWidget(self.bothEndsCheckBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.startButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton_2.setObjectName("startButton_2")
        self.horizontalLayout_14.addWidget(self.startButton_2)
        self.endButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.endButton_2.setObjectName("endButton_2")
        self.horizontalLayout_14.addWidget(self.endButton_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.releasesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.releasesLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.releasesLabel.setObjectName("releasesLabel")
        self.verticalLayout_6.addWidget(self.releasesLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.exCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.exCheckBox.setObjectName("exCheckBox")
        self.horizontalLayout_6.addWidget(self.exCheckBox)
        self.exLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.exLineEdit.setObjectName("exLineEdit")
        self.horizontalLayout_6.addWidget(self.exLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.eyCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.eyCheckBox.setObjectName("eyCheckBox")
        self.horizontalLayout_7.addWidget(self.eyCheckBox)
        self.eyLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.eyLineEdit.setObjectName("eyLineEdit")
        self.horizontalLayout_7.addWidget(self.eyLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ezCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.ezCheckBox.setObjectName("ezCheckBox")
        self.horizontalLayout_8.addWidget(self.ezCheckBox)
        self.ezLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ezLineEdit.setObjectName("ezLineEdit")
        self.horizontalLayout_8.addWidget(self.ezLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.phixCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.phixCheckBox.setObjectName("phixCheckBox")
        self.horizontalLayout_9.addWidget(self.phixCheckBox)
        self.phixLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.phixLineEdit.setObjectName("phixLineEdit")
        self.horizontalLayout_9.addWidget(self.phixLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.phiyCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.phiyCheckBox.setObjectName("phiyCheckBox")
        self.horizontalLayout_10.addWidget(self.phiyCheckBox)
        self.phiyLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.phiyLineEdit.setObjectName("phiyLineEdit")
        self.horizontalLayout_10.addWidget(self.phiyLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.phizCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.phizCheckBox.setObjectName("phizCheckBox")
        self.horizontalLayout_11.addWidget(self.phizCheckBox)
        self.phizLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.phizLineEdit.setObjectName("phizLineEdit")
        self.horizontalLayout_11.addWidget(self.phizLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.fixedButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fixedButton.setObjectName("fixedButton")
        self.horizontalLayout_12.addWidget(self.fixedButton)
        self.pinnedButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pinnedButton.setObjectName("pinnedButton")
        self.horizontalLayout_12.addWidget(self.pinnedButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.eccentricityLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.eccentricityLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eccentricityLabel.setObjectName("eccentricityLabel")
        self.verticalLayout_5.addWidget(self.eccentricityLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.yLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yLabel.setObjectName("yLabel")
        self.horizontalLayout_4.addWidget(self.yLabel)
        self.yLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yLineEdit.setObjectName("yLineEdit")
        self.horizontalLayout_4.addWidget(self.yLineEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.zLabel.setObjectName("zLabel")
        self.horizontalLayout_5.addWidget(self.zLabel)
        self.zLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.zLineEdit.setObjectName("zLineEdit")
        self.horizontalLayout_5.addWidget(self.zLineEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.gridLayoutWidget)
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.horizontalLayout_13.addWidget(self.openGLWidget_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.endConditionsTab, "")
        self.materialTab = QtWidgets.QWidget()
        self.materialTab.setObjectName("materialTab")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.materialTab)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 521, 421))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.treeView = QtWidgets.QTreeView(self.verticalLayoutWidget_10)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_16.addWidget(self.treeView)
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget_10)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_16.addWidget(self.tableView)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.newButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.newButton_2.setObjectName("newButton_2")
        self.horizontalLayout_17.addWidget(self.newButton_2)
        self.modifyButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.modifyButton_2.setObjectName("modifyButton_2")
        self.horizontalLayout_17.addWidget(self.modifyButton_2)
        self.deleteButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.deleteButton_2.setObjectName("deleteButton_2")
        self.horizontalLayout_17.addWidget(self.deleteButton_2)
        self.importButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.importButton_2.setObjectName("importButton_2")
        self.horizontalLayout_17.addWidget(self.importButton_2)
        self.exportButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.exportButton_2.setObjectName("exportButton_2")
        self.horizontalLayout_17.addWidget(self.exportButton_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.tabWidget.addTab(self.materialTab, "")
        self.verticalLayout_11.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget_11)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_11.addWidget(self.buttonBox)

        self.retranslateUi(editUnitWindow)
        self.tabWidget.setCurrentIndex(2)
        self.buttonBox.accepted.connect(editUnitWindow.accept)
        self.buttonBox.rejected.connect(editUnitWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(editUnitWindow)

    def retranslateUi(self, editUnitWindow):
        _translate = QtCore.QCoreApplication.translate
        editUnitWindow.setWindowTitle(_translate("editUnitWindow", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), _translate("editUnitWindow", "General"))
        self.bothEndsCheckBox_2.setText(_translate("editUnitWindow", "Same at both ends"))
        self.startButton.setText(_translate("editUnitWindow", "Start"))
        self.endButton.setText(_translate("editUnitWindow", "End"))
        self.newButton.setText(_translate("editUnitWindow", "New"))
        self.modifyButton.setText(_translate("editUnitWindow", "Modify"))
        self.deleteButton.setText(_translate("editUnitWindow", "Delete"))
        self.importButton.setText(_translate("editUnitWindow", "Import"))
        self.exportButton.setText(_translate("editUnitWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sectionTab), _translate("editUnitWindow", "Section"))
        self.eccLabel.setText(_translate("editUnitWindow", "Eccentricity in analytical model ............."))
        self.pushButton_5.setText(_translate("editUnitWindow", "PushButton"))
        self.pushButton_6.setText(_translate("editUnitWindow", "PushButton"))
        self.considerEccCheckBox.setText(_translate("editUnitWindow", "Consider eccentricity caused by cracking in cracked section analysis"))
        self.bothEndsCheckBox.setText(_translate("editUnitWindow", "The same at both ends"))
        self.startButton_2.setText(_translate("editUnitWindow", "Start"))
        self.endButton_2.setText(_translate("editUnitWindow", "End"))
        self.releasesLabel.setText(_translate("editUnitWindow", "Releases [kN/m, kNm/degree]"))
        self.exCheckBox.setText(_translate("editUnitWindow", "e,x\'..............................."))
        self.eyCheckBox.setText(_translate("editUnitWindow", "e,y\'..............................."))
        self.ezCheckBox.setText(_translate("editUnitWindow", "e,z\'..............................."))
        self.phixCheckBox.setText(_translate("editUnitWindow", "phi,x\'............................"))
        self.phiyCheckBox.setText(_translate("editUnitWindow", "phi,y\'............................"))
        self.phizCheckBox.setText(_translate("editUnitWindow", "phi,z\'............................"))
        self.fixedButton.setText(_translate("editUnitWindow", "fixed"))
        self.pinnedButton.setText(_translate("editUnitWindow", "pinned"))
        self.eccentricityLabel.setText(_translate("editUnitWindow", "Eccentricity [m]"))
        self.yLabel.setText(_translate("editUnitWindow", "y\'......"))
        self.zLabel.setText(_translate("editUnitWindow", "z\'......"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.endConditionsTab), _translate("editUnitWindow", "End Conditions"))
        self.newButton_2.setText(_translate("editUnitWindow", "New"))
        self.modifyButton_2.setText(_translate("editUnitWindow", "Modify"))
        self.deleteButton_2.setText(_translate("editUnitWindow", "Delete"))
        self.importButton_2.setText(_translate("editUnitWindow", "Import"))
        self.exportButton_2.setText(_translate("editUnitWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.materialTab), _translate("editUnitWindow", "Material"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editUnitWindow = QtWidgets.QDialog()
    ui = Ui_editUnitWindow()
    ui.setupUi(editUnitWindow)
    editUnitWindow.show()
    sys.exit(app.exec_())
