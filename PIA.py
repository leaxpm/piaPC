# PIA Programa Principal

def main():
    """
        **Main**
        This Module starts the script and controls everything with given arguments
    """
    import argparse
    import logging
    import Report
    parser = argparse.ArgumentParser(prog='Auto-Hacker', description='Accesorios Para Hacker', epilog='Usar baja su propio riesgo no nos hacemos responsables del uso incorrecto')
    parser.add_argument('-M','--metadata', help="Extraer Metadata de imagenes en un link('argumento --link requerido')",action='store_true')
    parser.add_argument('-L', '--link', help="Ingresar link de pagina web a analizar")
    parser.add_argument('-N','--nmap', help="Escanea de forma automatica el segmento de tu red privada ('Es requerido tener nmap instalado')",action='store_true')
    parser.add_argument('--public', help="Escanear IP Publica",action='store_true',default=False)
    parser.add_argument('--private', help="Escanear Segmento de IPS Privadas",action='store_true',default=False)
    parser.add_argument('-FTP','--ftp', help="Enumera el contenido de un servicio FTP('argumento --host requerido')",action='store_true')
    parser.add_argument('--host', help="Host FTP a conectar")
    parser.add_argument('-P','--password', help="Password para conexion FTP")
    parser.add_argument('-U','--user', help="User para conexion FTP")
    parser.add_argument('--anonymous', help="Anonymous conexion FTP",action='store_true')
    parser.add_argument('-H','--hunter', help="Busqueda de correos sobre el nombre de una organizacion ('argumento --organizacion y --apiKey requerido')",action='store_true')
    parser.add_argument('-O','--organizacion', help="Nombre de la organizacion para buscar correos")
    parser.add_argument('--apiKey', help="Api Key token de la aplicacion Hunter.IO")
    args = parser.parse_args()
    if args.metadata:
        if args.link:
            import metadataScrapper
            logging.info("Metadata Scan Started on " + args.link)
            print(Report.report(metadataScrapper.Metadata(args.link),"Metadata Scrapper"))
        else:
            logging.warning("Falta de Argumentos")
            parser.error("--metadata requires --link.")
    elif args.nmap:
        import autoNmap
        if args.public:
            logging.info("Nmap Scan Public Started")
            print(Report.report(autoNmap.exec(scan="public"),"Nmap Public Scan"))
        elif args.private:
            logging.info("Nmap Scan Private Started")
            print(Report.report(autoNmap.exec(scan="private"),"Nmap Private Scan"))
        else:
            logging.warning("Falta de Argumentos")
            parser.error("--nmap requires --private or --public.")
    elif args.ftp:
        import ftpScanner
        if args.host:
            if args.host and args.user and args.password:
                logging.info("FTP Dir Scanner Started")
                print(Report.report(ftpScanner.dir(args.host,args.user,args.password,args.anonymous),"FTP Scanner Authenticated"))
            elif args.anonymous:
                logging.info("FTP Dir Scanner Started")
                print(Report.report(ftpScanner.dir(args.host,"","",args.anonymous),"FTP Scanner Anonymous"))
        else:
            logging.warning("Falta de Argumentos")
            parser.error("--ftp requires --host and --user --password or --anonymous.")
    elif args.hunter:
        import hunter
        if args.organizacion and args.apiKey:
            logging.info("Hunter Scan Started Over: "+ args.organizacion)
            print(Report.report(hunter.main(args.apiKey,args.organizacion),"Hunter Scan"))
        else:
            logging.warning("Falta de Argumentos")
            parser.error("--hunter requires --organizacion and --apiKey.")
    else:
        helpMenu = f"{parser.print_help()}".replace("None","")
        logging.warning(helpMenu)

if __name__ == '__main__':
    main()
