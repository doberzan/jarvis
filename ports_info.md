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
## PORT 139 | SMB/netbios-ssn (Server Message Block/Network Basic Input Output System)
Description: This port is used as a way for windows to communicate to other computers in a network. It holds lots of useful information and can be queried with 'nbtstat <params>'.
- Protocol: `TCP`
  - Software (default on windows):
    - Samba (Network Directory Sharing):
      - OS: `Unix`
			
## PORT 1433 | MSSQL/ms-sql-s (Microsoft Structured Query Language)
- Protocol: `TCP,UDP`
- Description: Microsoft SQL Database query port
	
## PORT 3260 | ISCSI (Internet Small Computer Systems Interface),
- Protocol: `TCP`
- Description: ISCSI is a service that provides network drive connectivity over a lan/wan, but the clients treat the drive as physicaly connected device.
  - OS: `Windows`
## PORT 5432 | PostgreSQL
- Protocol: `TCP`
- Description: Serves as a SQL database similar to MSSQL but multiplatform.
  - OS: `Windows, Unix`

## PORT 9091 | Citrix Mapping and XMTP (XML MIME Transport Protocol) and Openfire Administration Console
- Protocol: `TCP`
- Citrix Description: Used to refresh, update, and query Citrix information/devices/administration
- XMTP Description: Transport XML MIME types over network
- Openfire Administration: Admin page for Openfire instant messaging and groupchat server.
