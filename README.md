N.B

1) There are two controllers and two repositories for games. There are also two repositories for teams. This is because as there are two groups in the competition, there are two tables for teams alone in the database.
- In these multiple files, the code is exactly the same, apart from the variable names being different. This way each object is handled in the same way, but kept separate if they are within different groups.
- The rationale for this is that I am sorting the way in which the teams are displayed in the league table based on how many points they have. A team may be at the top of their group but have less points than the winner of the other group. I want the table to reflect this behaviour.