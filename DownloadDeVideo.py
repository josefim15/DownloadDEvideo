from pytube import YouTube
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

def baixar_video():    
    try:
        #COLANDO O LINK DO VÍDEO E DIRETORIO
        
        url = file.lineEdit.text()
        diretorio = file.lineEdit_2.text()
        tube = YouTube(url)
        
        botaoAudio = file.radioButton.isChecked()
        botaoVideo = file.radioButton_2.isChecked()
        
        if botaoVideo:
            video = tube.streams.get_highest_resolution()
            video.download(diretorio)
            msg = QMessageBox()
            msg.setWindowTitle('DOWNLOAD')
            msg.setText('Download concluído')
            msg.setIcon(QMessageBox.Information)
                
            x = msg.exec_()
            print('OK')
            
        elif botaoAudio:
            audio = tube.streams.filter(only_audio=True).first()
            RemoverFormatoMpfour = audio.download(output_path=diretorio)
            
            base, ext = os.path.splitext(RemoverFormatoMpfour)
            NovoFormatoDeArquivo = base + '.mp3'
            os.rename(RemoverFormatoMpfour, NovoFormatoDeArquivo)
            
            msg = QMessageBox()
            msg.setWindowTitle('DOWNLOAD')
            msg.setText('Download concluído')
            msg.setIcon(QMessageBox.Information)
                
            x = msg.exec_()
            print('OK')
    
    except:
        msgError = QMessageBox()
        msgError.setWindowTitle('Erro')
        msgError.setText('Houve um erro')
        msgError.setIcon(QMessageBox.Warning)
        msgError.exec_()
            
app=QtWidgets.QApplication([])
file=uic.loadUi('baixar.ui')
file.pushButton.clicked.connect(baixar_video)

file.show()
app.exec()