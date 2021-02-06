
## Glossary
    
- **Match** is an istance of a specific case     

- **play_one** method to go through one case

- **Session**: has player name and it allows to pass (by **play_all** method) all the 10 cases



## Database insight

- **page**: id of situation
- **case**: one of the 10 (possile) cases
- **parent**: the origin of the page. Set to 0 if it is the first page of the case
- **goto**: force link to another previous page, if solution isn't sadisactory
- **level**: not used
- **label**: not used
- **choice**: set to True if the paga need a choice by the user
- **end**:  set to True if the macht has been completed
- **msg_pre**: message to be shown in parent page
- **msg_actual**: message to be shown in the page itself