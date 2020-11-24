
 PIA: AutoHacker
------------------------------------------------------------------------------------------------


Overview on How to Run 
------------------------------------------------------------------------------------------------ 
     1. Install requirements.txt
     2. Run PIA.py -h


Setup procedure
------------------------------------------------------------------------------------------------


A. Configure project environment (Create a Virtual Environment)
------------------------------------------------------------------------------------------------

     1. Create a Python Virtual Environment
         - Install virtualenv::

             sudo pip install virtualenv

         - Create virtialenv::

              virtualenv -p python3 <name of virtualenv>
    
         - Install pipenv::

              sudo pip install pipenv

         - Create virtialenv::

              pipenv shell

         - Install requirements::

              pip install -r requirements.txt

        

B. Run PIA.py
------------------------------------------------------------------------------------------------

    python3 PIA.py


C. Run Hunter Module
------------------------------------------------------------------------------------------------

    1. You need to login in https://hunter.io/
    2. Find your api key on https://hunter.io/api
    3. Use --apiKey and add yours


D. Run Metadata Module
------------------------------------------------------------------------------------------------

    1. You need to use argument -M or --metadata
    2. Use --link and add the link you wanna scrap
    3. Wait the images and the output on images/ folder

  
D. Run FTP Module
------------------------------------------------------------------------------------------------

    1. You need to use argument -FTP or --ftp
    2. FTP Module requires a host given by --host
    3. A) User and Password must be given with --user and --password
    4. B) Use --anonymous for Anonymous login


E. Run Nmap Module
------------------------------------------------------------------------------------------------

    1. To use -N or --nmap is required to install Nmap Follow Step E-A
    2. A) Use --public for Scan your public IP
    3. B) Use --private to Scan your complete private mask
    

E-A. Install Nmap 
------------------------------------------------------------------------------------------------

    1. Follow this link for official info https://nmap.org/


Documentation
------------------------------------------------------------------------------------------------

    - Documentation generated using Sphinx.

