## PORT 21 | FTP (File Transfer Protocol)
Description: This port is used to transfer files over the network.
- Protocol: `TCP`
  - Common Server Software:
    - *vsftpd*:
      - OS: `Unix`
      - Guest: `anonymous anonymous`
    - *ProFTPD*:
      - OS: `Unix, Windows`
      - Guest: `anonymous/ftp <email>`
    - *CerberusFTP*:   
      - OS: `Windows-based`
      - Guest: `None`
	
## PORT 25 | SMTP (Simple Mail Transfer Protocol)
Description: This port is used to receive and send emails between mail servers NOT to be confused with IMAP or POP3 which are used to send mail to clients.
- Protocal: `TCP`
  - **Common Server Software**:
    - *Postfix*: 
      - OS: `Unix`
    - *Qmail*:
      - OS: `Unix`
    - *TurboSMTP*:
      - OS: `Windows`
## PORT 139 | SMB/netbios-ssn
Description: This port is used as a way for windows to communicate to other computers in a network. It holds lots of useful information and can be queried with 'nbtstat <params>'.
- Protocol: `TCP`
  - Software (default on windows):
  - Samba (Network Directory Sharing):
    - OS: `Unix`
			
## PORT 1433 | MSSQL/ms-sql-s,
- Protocol: `TCP,UDP`
- Description: `Microsoft SQL Database query port`
	
## PORT 3260 | ISCSI (Internet Small Computer Systems Interface),
- Protocol: `TCP`
- Description: ISCSI is a service that provides network drive connectivity over a lan/wan, but the clients treat the drive as physicaly connected device.
  - OS: `Windows`
## PORT 5432,
## PORT 9091
