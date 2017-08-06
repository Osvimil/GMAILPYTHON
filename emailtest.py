import smtplib
contenido = 'we are sipply the best company'
correo = smtplib.SMTP('smtp.gmail.com',587)
correo.ehlo()
correo.starttls()
correo.login('quienenvia@gmail.com','contrasena')
correo.sendmail('quienenvia@gmail.com','quienrecibe@gmail.com',contenido)
correo.sendmail('quienenvia@gmail.com','quienrecibe@gmail.com',contenido)
correo.close()
