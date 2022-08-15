from cryptography.fernet import Fernet
from PyQt6 import QtCore, QtGui, QtWidgets
import pathlib

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 235, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 245, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 117, 119))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 157, 159))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 235, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 245, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 117, 119))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 235, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 245, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 117, 119))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 157, 159))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 117, 119))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 117, 119))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 235, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 235, 239))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        Form.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/data-encryption.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_encrypt = QtWidgets.QPushButton(Form)
        self.Button_encrypt.setObjectName("Button_encrypt")
        self.horizontalLayout.addWidget(self.Button_encrypt)
        self.Button_decrypt = QtWidgets.QPushButton(Form)
        self.Button_decrypt.setObjectName("Button_decrypt")
        self.horizontalLayout.addWidget(self.Button_decrypt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_create_key = QtWidgets.QPushButton(Form)
        self.Button_create_key.setObjectName("Button_create_key")
        self.horizontalLayout_2.addWidget(self.Button_create_key)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.Button_load_key = QtWidgets.QPushButton(Form)
        self.Button_load_key.setObjectName("Button_load_key")
        self.horizontalLayout_2.addWidget(self.Button_load_key)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(6, 23, 600, 700))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.groupBox)
        self.Button_save = QtWidgets.QPushButton(Form)
        self.Button_save.setObjectName("Button_save")
        self.verticalLayout.addWidget(self.Button_save)
        
        # varible 
        self.file_loaded = False
        self.encrypt_loaded = False
        self.key_create = False
        self.load_key = False
        self.load_file_name = ""
        self.encrypt_file = ""
        self.text_for_decrypt = ""
        self.key = ""

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # button click
        self.Button_encrypt.clicked.connect(self.btn_encrypt)
        self.Button_create_key.clicked.connect(self.btn_create_key)
        self.Button_save.clicked.connect(self.btn_save)
        self.Button_decrypt.clicked.connect(self.btn_decrypt)
        self.Button_load_key.clicked.connect(self.btn_load_key)
        
    # load orginal file 
    def btn_encrypt(self):
        """
        Upload text file for encryption
        """
        loc = pathlib.Path("./file/")
        _load_file_name = QtWidgets.QFileDialog.getOpenFileName(None, "open file", loc.name)
        if _load_file_name[0]:
            _load_file_name = _load_file_name[0]
            file = open(_load_file_name, "r",encoding='latin-1')
            file_text = file.read()
            file.close()
            self.label.setText(file_text)
            self.file_loaded = True
            self.encrypt_loaded = False
            self.load_file_name = _load_file_name
        
    # create key
    def btn_create_key(self):
        """
        Creating a new key for encryption
        """
        if self.file_loaded:
            self.key = Fernet.generate_key()
            fer = Fernet(self.key)
            if self.load_file_name:
                with open(self.load_file_name,"rb") as _file:
                    _file = _file.read()
                self.encrypt_file = fer.encrypt(_file)
                self.groupBox.setTitle("encrypt text")
                self.label.setText(str(self.encrypt_file))
                self.key_create = True
                self.load_key = False
                self.lineEdit.setText(str(self.key))
        else:
            _txt = " First, from 'encrypt file' select the file you want to encrypt"
            self.show_popup(_txt)

    # save file and key 
    def btn_save(self):
        """
            Save the encrypted file with the new key.
            If the key was already created, it will not save it.
            If the encrypted file is called, it saves it after decoding.
        """
        if self.key_create or self.load_key and self.file_loaded:
            with open(self.load_file_name+"_encrypt.txt","wb") as encry_file:
                encry_file.write(self.encrypt_file)
            if self.key_create:
                with open(self.load_file_name+"_key.key","wb") as key_file:
                    key_file.write(self.key)  
            _txt = f'Your encrypted file: {self.load_file_name+"_encrypt.txt"} has been saved.\n encryption key: {self.load_file_name+"_key.key"} saved.'
            self.show_popup(_txt)
        elif self.load_key and self.encrypt_loaded:
            fer = Fernet(self.key)
            decrypt = fer.decrypt(self.text_for_decrypt)
            decrypt =  str(decrypt.decode('latin-1'))
            loc = pathlib.Path("./file/")
            _save_file_name = QtWidgets.QFileDialog.getSaveFileName(None, "save file", loc.name)
            if _save_file_name[0]:
                _save_file_name = _save_file_name[0]
                file = open(_save_file_name, "w",encoding='latin-1')
                file.write(str(decrypt))
                _txt = _txt = f'Your decrypted file: {_save_file_name} has been saved'
                self.show_popup(_txt)
        else:
            _txt = "To save, first open the file, then create the key or load the previous key, then you can save."
            self.show_popup(_txt)

    # load encrypt file to decrypt 
    def btn_decrypt(self):
        """
            Open the encrypted file to perform decryption
        """
        loc = pathlib.Path("./file/")
        _load_file_name = QtWidgets.QFileDialog.getOpenFileName(None, "open file", loc.name)
        if _load_file_name[0]:
            _load_file_name = _load_file_name[0]
            with open(_load_file_name,"rb") as _file:
                self.text_for_decrypt = _file.read()
            self.encrypt_loaded = True
            self.file_loaded = False
            self.groupBox.setTitle("encrypt text")
            self.label.setText(str(self.text_for_decrypt))
            _txt = "Select the appropriate key to decrypt"
            self.show_popup(_txt)

    # load key file
    def btn_load_key(self):
        """
            Upload key for encryption or decryption
            If the file is encrypted, the key will decrypt it
            If the file is not encrypted, the key will encrypt it
        """
        if self.encrypt_loaded :
            loc = pathlib.Path("./file/")
            _load_key_file = QtWidgets.QFileDialog.getOpenFileName(None, "open file", loc.name)
            if _load_key_file[0]:
                _load_key_file = _load_key_file[0]
                with open(_load_key_file,"rb") as _file:
                    text_for_key = _file.read()
                self.lineEdit.setText(str(text_for_key))
                self.key = text_for_key
                fer = Fernet(self.key)
                decrypt = fer.decrypt(self.text_for_decrypt)
                self.groupBox.setTitle("decrypt text")
                self.label.setText(str(decrypt.decode('latin-1')))
                self.load_key = True
                self.key_create = False
        elif self.file_loaded:
            loc = pathlib.Path("./file/")
            _load_key_file = QtWidgets.QFileDialog.getOpenFileName(None, "open file", loc.name)
            if _load_key_file[0]:
                _load_key_file = _load_key_file[0]
                with open(_load_key_file,"rb") as _file:
                    text_for_key = _file.read()
                self.lineEdit.setText(str(text_for_key))
                self.key = text_for_key
                fer = Fernet(self.key)
                with open(self.load_file_name,"rb") as _file:
                    _file = _file.read()
                self.encrypt_file = fer.encrypt(_file)
                self.groupBox.setTitle("encrypt text")
                self.label.setText(str(self.encrypt_file))
                self.key_create = False
                self.load_key = True
                self.lineEdit.setText(str(self.key))

    # show popup
    def show_popup(self, txt):
        """
            Display messages to perform operations
        """
        massage_box = QtWidgets.QMessageBox()
        massage_box.setWindowTitle("message")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/data-encryption.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        massage_box.setWindowIcon(icon)
        massage_box.setText(txt)
        massage_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        massage_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        massage_box.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "data encryption"))
        Form.setGeometry(QtCore.QRect(400, 100, 600, 480))
        self.Button_encrypt.setText(_translate("Form", "make encrypt file"))
        self.Button_decrypt.setText(_translate("Form", "make decrypt file"))
        self.Button_create_key.setText(_translate("Form", "create key"))
        self.lineEdit.setPlaceholderText(_translate("Form", "key name"))
        self.Button_load_key.setText(_translate("Form", "load key"))
        self.groupBox.setTitle(_translate("Form", "text"))
        self.Button_save.setText(_translate("Form", "save file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
