## PORT 21 | FTP(File Transfer Protocal),
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
	
## PORT 25 | SMTP(Simple Mail Transfer Protocal),
- Protocal: `TCP`
- Common Server Software:
- *Postfix*: 
  - OS: `Unix`
- *Qmail*:
  - OS: `Unix`
- *TurboSMTP*:
  - OS: `Windows`
## PORT 139 | SMB/netbios-ssn,
	Protocal: `TCP`
	Software (default on windows):
		Samba (Network Directory Sharing):
			OS: `Unix`
	nbtstat - Command to "debug" and gain info on a target windows machine
			
## PORT 1433 | MSSQL/ms-sql-s,
	Protocal: `TCP,UDP`
	Description: `Microsoft SQL Database query port`
	
## PORT 3260,
## PORT 5432,
## PORT 9091
