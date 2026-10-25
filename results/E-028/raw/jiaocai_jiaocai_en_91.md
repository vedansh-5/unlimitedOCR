<|det|>table [140, 85, 622, 137]<|/det|><table><tr><td>UAT</td><td>C++</td></tr><tr><td>UAT</td><td>Finance</td></tr></table>
<|det|>text [145, 141, 851, 175]<|/det|>In addition, we define that “an employee fits a job” if and only if the employee has all skills that are needed by the job.
<|det|>text [146, 181, 704, 199]<|/det|>Please write relational algebra expressions for the following queries.
<|det|>text [147, 204, 811, 237]<|/det|>1) Find the name of female employees who have at least one skill needed by the "DEV" job.
<|det|>text [146, 244, 615, 262]<|/det|>2) Find the names of employees who fit the "DEV" job.
<|det|>title [146, 269, 553, 289]<|/det|>2. SQL Query (20 points, 5 points each)
<|det|>text [145, 295, 836, 329]<|/det|>Consider the relational schemas given in problem 1, please write SQL statements to meet the following requests.
<|det|>text [147, 335, 546, 351]<|/det|>1) Find the employees who have not any skills.
<|det|>text [146, 357, 637, 374]<|/det|>2) Find the jobs that need at least "Java" and "C++" skills.
<|det|>text [146, 381, 844, 414]<|/det|>3) Find the names of employees who have the maximum number of skills among all employees.
<|det|>text [146, 421, 684, 437]<|/det|>4) Find the employees who fit both the "DEV" and "UAT" jobs.
<|det|>title [146, 446, 456, 465]<|/det|>3. Embedded SQL (10 points)
<|det|>text [145, 471, 832, 521]<|/det|>Based on the schemas defined in problem 1, the following embedded SQL program accepts the id of an employee as input, and output all skills of the employee. Please fill in the blanks of the program.
<|det|>text [146, 528, 212, 544]<|/det|>main()
<|det|>text [149, 551, 830, 901]<|/det|>{ EXEC SQL INCLUDE SQLCA;
EXEC SQL BEGIN DECLARE SECTION;
char id[10]; char skill [20];
EXEC SQL END DECLARE SECTION;
EXEC SQL CONNECT TO skill_db USER use1 USING password1;
EXEC SQL DECLARE skill_cursor CURSOR for ①;
printf("please input employee id :");
scanf("%s", id);
EXEC SQL ②;
for (; ;)
{ EXEC SQL ③;
if (④) break;
printf("%s\n", id);
