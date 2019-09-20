## PORT 21 | FTP (File Transfer Protocal)
Description: This port is used to transfer files over the network.
- Protocal: `TCP`
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
	
## PORT 25 | SMTP (Simple Mail Transfer Protocal)
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
- Protocal: `TCP`
  - Software (default on windows):
  - Samba (Network Directory Sharing):
    - OS: `Unix`
			
## PORT 1433 | MSSQL/ms-sql-s,
	Protocal: `TCP,UDP`
	Description: `Microsoft SQL Database query port`
	
## PORT 3260,
## PORT 5432,
## PORT 9091
