
//  6 - dars
// #include <stdio.h>
// #include <string.h>
// int main() {
//     //shopping
//     char item[50]="";
//     float price = 0.0f;
//     int miqdor = 0;
//     char valyuta= '$';
//     float total = 0.0f;

//     printf("nima olmoqchisiz?: ");
//     fgets(item, sizeof(item), stdin);
//     item[strlen(item) - 1] = '\0';

//     printf("qanchadan?: ");
//     scanf("%f", &price);

//     printf("nechta?: ");
//     scanf("%d", &miqdor);

//     total = price * miqdor;

//     printf("\nsiz %d ta %s sotib oldingiz\n", miqdor, item);
//     printf("umumiy: %c%.2f", valyuta, total);

//  7-dars

// #include <stdio.h>
// #include <string.h>
// int main() {
//     char noun[50] = "";
//     char verb[50] = "";
//     char adjective1[50] = "";
//     char adjective2[50] = "";
//     char adjective3[50] = "";

//     printf("enter an ajective (describtion); ");
//     fgets(adjective1, sizeof(adjective1), stdin);
//     adjective1[strlen(adjective1) - 1]='\0';

//     printf("enter an noun (animal or human); ");
//     fgets(noun, sizeof(noun), stdin);
//     noun[strlen(noun) - 1]='\0';

//     printf("enter an ajective (describtion); ");
//     fgets(adjective2, sizeof(adjective2), stdin);
//     adjective2[strlen(adjective2) - 1]='\0';

//     printf("enter a verb  (-ing); ");
//     fgets(verb, sizeof(verb), stdin);
//     verb[strlen(verb) - 1]='\0';

//     printf("enter an ajective (describtion): ");
//     fgets(adjective3, sizeof(adjective3), stdin);
//     adjective3[strlen(adjective3) - 1]='\0';

//     printf("%s\n", adjective1);
//     printf("%s\n", adjective2);
//     printf("%s\n", adjective3);
//     printf("%s\n", noun);
//     printf("%s\n", verb);
//     printf("Men kecha juda katta %s kurashga bordim u yerda %sni ko'rdim.\nU %s bilan %s edi.\nO'shanda u o'zini %sini ko'rsatdi.\n ", adjective1,noun, adjective2, verb, adjective3);

//     return 0;
// }

// //   8 - dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>

// int main() {

//     float x = 2;
//     // x=sqrt(x); ildiz chiqarish

//     // x= pow(x, 3); darajaga ko'tarish

//     // x= round(x); butun qilish pastga olib tushadi

//     // x = ceil(x); ceil() doimo eng yaqin katta yoki teng butun songa boradi

//     // x=abs(x); noldan qancha uzoqligini ko'rsatadi

//     // x=log(x); ln(x)

//     // x=sin(x); sinus radianda

//     // x=cos(x); cosinus

//     // x=tan(x); tanginus

//     printf("%f",x );

//     return 0;
// }

//  9- dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>

// int main() {

//     double radius = 0.0;
//     double area = 0.0;
//     double surfaceArea= 0.0;
//     const double PI = 3.14159;
//     double volume = 0.0;

//     printf("radiusni kiriting: ");
//     scanf("%lf",&radius);

//     area= PI * pow(radius, 2);
//     surfaceArea = 4*PI* pow(radius, 4);
//     volume = (4.0/3.0)* PI* pow(radius,3);

//     printf("s = %.2lf\n", area);
//     printf("the surface area: %.2lf\n", surfaceArea);
//     printf("the volume: %.2lf\n", volume);

//     return 0;
// }

//  10 - dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>

// int main() {
//     double principal = 0.0;
//     double rate = 0.0;
//     int years = 0;
//     int timescoumpounded = 0;
//     double total = 0.0;

//     printf("compound interest calculator");

//     printf("enter the prinsipal: ");
//     scanf("%lf", &principal);

//     printf("enter the rate: ");
//     scanf("%lf", &rate);
//     rate=rate/100;

//     printf("enter the number of years: ");
//     scanf("%d", &years);

//     printf("compounded per year: ");
//     scanf("%d", &timescoumpounded);

//     total= principal*pow(1+rate/timescoumpounded, timescoumpounded*years);

//     printf("the total will be: %.2lf", total);

//     return 0;
// }

//  11 - dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// int main() {

//     // int age = 0;

//     // printf("enter your age: ");
//     // scanf("%d", &age);

//     // if(age >=70){
//     //     printf("you are a senior");
//     // }
//     // else if(age>=18){
//     //     printf("you are an adult");
//     // }
//     // else if (age<0){
//     //     printf("eror");
//     // }
//     // else{
//     //     printf("you are a child");
//     // }

//     // bool isstudent = true;

//     // if (isstudent){
//     //     printf("youb are a student");
//     // }
//     // else{
//     //     printf("you are darmayit");
//     // }

//     char name[50] = "";

//     printf("enter your name: ");
//     fgets(name, sizeof (name), stdin);
//     name[strlen(name)- 1 ] = '\0';

//     if (strlen(name) == 0){
//         printf("galvars ismingni kirit");
//     }
//     else {
//         printf("Hello %s!", name);
//     }

//     return 0;
// }

//  12 - dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// int main() {

//     int choice = 0;
//     float pounds = 0.0f;
//     float kilograms = 0.0f;

//     printf("weight conversion calculator\n");
//     printf("1. kg to pounds\n");
//     printf("2. pounds to kg\n");
//     printf("what is your choice (1 or 2): ");
//     scanf("%d", &choice);

//     if (choice ==1 ){
//         printf("enter your weight in kg: ");
//         scanf("%f", &kilograms);
//         pounds = kilograms*2.205;
//         printf("%.2f kilograms is equel to %.2f pounds",  kilograms, pounds);

//     }
//     else if (choice ==2){
//         printf("enter your weight in pounds: ");
//         scanf("%f", &pounds);
//         kilograms = pounds/2.05;
//         printf("%.2f pounds is equel to %.2f kilograms", pounds, kilograms);

//     }
//     else{
//         printf("invalid choice");
//     }

//     return 0;
// }

//  14-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// int main() {

//     char dayofWeek = '\0';

//     printf("enter the day of the week(M-U); ");
//     scanf("%c", &dayofWeek);

//     switch(dayofWeek){
//         case 'M':
//             printf("it is Monday");
//             break;
//         case 'T':
//             printf("it is Tuesday");
//             break;
//         case 'W':
//             printf("it is Wednesday");
//             break;
//         case 'R':
//             printf("it is Thursday");
//             break;
//         case 'F':
//             printf("it is Friday");
//             break;
//         case 'S':
//             printf("it is Saturday");
//             break;
//         case 'U':
//             printf("it is Sunday");
//             break;
//         default:
//             printf("enter a number in(M-U)");

//     }

//     return 0;
// }

//  15 - dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// int main() {

//     float price = 10;
//     bool isstudent = false;
//     bool issenior=true;

//     if (isstudent){
//         if (issenior){
//             printf("you get a senior dicount of 20%\n");
//             printf("you get a student dicount of 10%\n");
//             price*=0.7;
//         }
//         else{
//             printf("you get a student dicount of 10%\n");
//             price*=0.9;
//         }
//     }
//     else if (issenior){
//         printf("you get a senior dicount of 20%\n");
//         price*=0.8;

//     }
//     printf("the price is $%.2f", price);

//     return 0;
// }

//  16-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// int main() {

//     char operator = '\0';
//     double num1= 0.0;
//     double num2= 0.0;
//     double result= 0.0;

//     printf("enter the first number: ");
//     scanf("%lf",&num1);

//     printf("enter the op(+-/*): ");
//     scanf(" %c",&operator);

//     printf("enter the second number: ");
//     scanf("%lf",&num2);

//     switch (operator){
//         case '+':
//             result= num1+num2;
//             break;
//         case '-':
//             result= num1-num2;
//             break;
//         case '*':
//             result= num1*num2;
//             break;
//         case '/':
//             if (num2==0){
//                 printf("you can't do that");
//             }
//             result= num1/num2;
//             break;
//         default:
//             printf("dabba (+-*/)dan bittasini kirit\n");

//     }
//     printf("the result is %.3lf", result);

//     return 0;
// }

//  17-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// int main() {

//     int temp=177;
// //  && - and
// // || - or
// //

//     // if (temp<0 || temp>30){
//     //     printf("the temperature is bad");

//     // }
//     // else {
//     //     printf("the temperature is good");
//     // }

//     bool issunny= false;

//     if (!issunny){
//         printf("it is not sunny outside");

//     }
//     else{
//         printf("it is  sunny outside");
//     }
//     return 0;
// }

//  18-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// void happybirthday( char name[], int age){
//     printf("happy birthy!%s\n",name);
//     printf("happy birthy!\n");
//     printf("happy birthy!%d\n", age);
// }

// int main() {

//     int age = 0;
//     char name[50]="";

//     printf("enter your name: ");
//     fgets(name, sizeof(name), stdin);
//     name[strlen(name)-1]='\0';

//     printf("enter your age; ");
//     scanf("%d",&age);
//     happybirthday(name ,age);

//     return 0;
// }

//  19-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// // double cube(double num){
// //     double result = num*num*num;
// //     return result;
// // }

// // double square(double num){
// //     double result = num*num;
// //     return result;
// // // }
// //    int main() {

// //     double x= square(3.32);
// //     double y = cube (3.14);

// //     printf("%.3lf\n",x);
// //     printf("%.3lf",y);

// //     return 0;
// // }

// bool agecheck(int age){
//     if (age>18){
//         return true;
//     }
//     else {
//         return false;
//     }
// }

//    int main() {

//     int age = 17;

//     if (agecheck(age)){
//         printf(" you can run");

//     }
//     else {
//         printf("it is early kid");
//     }

//     return 0;
// }

//  21 - dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

// void hello(char name[] , int age );

// bool ageCheck(int age);

//    int main() {

//     hello("jahongir", 19);
//     if (ageCheck(19)){
//         printf("you are hired");

//     }
//     else {
//         printf("you are just a kid");
//     }

//     return 0;
// }
// void hello(char name[] , int age ){
//     printf("hello %s\n", name);
//     printf("you are %d years old\n", age);
// }

// bool ageCheck(int age){
//     return age>=16;
// }

//  22-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>

//    int main() {

//     // int number =1;

//     // do{
//     //     printf("enter a number; ");
//     //     scanf("%d", &number);
//     // }    while (number <=0);

//     char name [50]="";

//     printf("enter your name: ");
//     fgets (name,sizeof(name),stdin);
//     name[strlen(name)-1]='\0';

//     while (strlen(name)==0){
//         printf("name cannot be empty, xuyet karsimi suka!!");
//         fgets (name,sizeof(name),stdin);
//         name[strlen(name)-1]='\0';
//     }

//     return 0;
// }

// // // 23-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>

//    int main() {

//     for ( int i=10; i>=0; i-=1){
//         Sleep(1000);
//         printf("%d\n", i);
//     }

//     printf("Happy new year!!!");

//     return 0;
// }

//  24-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>

//    int main() {
//     for (int i = 1; i<=10; i++){

//         if (i==1){
//             continue;
//         }
//         printf("%d\n",i );
//     }

//     return 0;
// }

// 25-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>

//    int main() {

//     // for (int i = 1; i<4;i++){
//     //     for (int j = 1; j<=10; j++){
//     //         printf(" %d ", j);
//     //     }
//     //     printf("\n");
//     // }

//     // for (int i = 1; i<=10;i++){
//     //     for (int j = 1; j<=10; j++){
//     //         printf("%3d ", j*i);
//     //     }
//     //     printf("\n");
//     // }

//     int columns=0;
//     int rows =0;
//     char symbol= '\0';

//     printf("# of columns: ");
//     scanf("%d", &columns);

//     printf("symbol?: ");
//     scanf(" %c", &symbol);

//     printf("# of rows: ");
//     scanf("%d", &rows);

//     for (int i = 1; i<=rows;i++){
//         for (int j = 1; j<=columns; j++){
//             printf("%c ", symbol);
//         }
//         printf("\n");
//     }

//     return 0;
// }

//  26-27-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// int main()
// {
//     // srand(time(NULL));

//     // // printf("%d", RAND_MAX);

//     // int randnum = rand() % 100;  # bunda 0 dan 100 gacha sonlar kiradi

//     // printf("%d", randnum);


//     srand(time(NULL));

//     int guess = 0;
//     int tries = 0;

//     int min = 10;
//     int max = 90;

//     int answer = (rand ()% max) + min;

     
//     do {
//         printf("guess betwen %d - %d: ", min, max);
//         scanf("%d", &guess);
//         tries++;

//         if (answer>guess){
//             printf("too low!\n");
        
//         }
//         else if (answer < guess){
//             printf("too high!\n");
//         }
//         else ("correct!!!\n");


//     }while(answer!=guess);


//     printf("the answer was %d\n", answer);
//     printf("it took you %d tries\n", tries);

//     return 0;
// }


//  29-dars



// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// int getcompchoice();
// int getuserchoice();
// void checkwinner(int userchoice, int compchoice);

// int main()
// {
//     //  Tosh qaychi qog'oz

//     srand(time(NULL));

//     int compchoice= getcompchoice();
//     int userchoice= getuserchoice();


//     printf("*** ROCK PAPER SCISSORS***");





//     return 0;
// }
// int getcompchoice(){

//         return  (rand()%3)+1;
// }


// int getuserchoice(){
//     int choice =0;

//         return 0; 

// }
    


// void checkwinner(int userchoice, int compchoice){
//         return 0;
// }


// // 31-dars Arrays





// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>


// int main(){
    

//     int numbers[]= {0,1,2,3,4,5};
//     char grades[] =  { 'a','b', 'c', 'd'};
//     char name[] = "Jahongir";

//     printf("%d", sizeof(numbers[1]));


//     int size= sizeof(numbers)/sizeof(numbers[0]);
//     numbers[2]=10;


//     for (int i = 0; i<size ; i++){
//         printf("%d\n", numbers[i]);
//     }

    




//     return 0;
// }




// 29-dars





// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>


// void checkbalance(float balance);
// float deposit ();
// float withdraw(float balance);

// int main(){
    
//     int choice = 0;

//     float balance=0.0f;

//     printf("**** WELCOME TO THE ISLAMIC BANK ****\n");

//     do{
//         printf("  SELECT:  \n");
//         printf("1.check balance\n");
//         printf("2. deposit money\n");
//         printf("3. withdraw money\n");
//         printf("4.exit\n");
//         printf("enter your choice: ");
//         scanf("%d", &choice);
   


//     switch(choice){
//         case 1:
//             checkbalance(balance);
//             break;
//         case 2:
//             balance = balance + deposit();
//             break;
//         case 3:
//             balance = balance - withdraw(balance);
//             break;
//         case 4:
//             printf("\nTHANK YOU FOR USING THE ISLAMIC BANK!!!\n");
//             break;
//         default:
//             printf("\ninvalid choice!\n");


//         }
//         }while (choice!=4);
    
//     return 0;
// }

// void checkbalance(float balance){


//     printf("your current balance is: $%.2f\n", balance);
// }

// float deposit(){

    
//     float amount=0.0f;

   
//     printf("how much do you want to deposit: $");
//     scanf("%f", &amount);

//     if (amount>0){
//         printf("successfully deposited $%.2f\n", amount);
//         return amount;
//     }
//     else {
//         printf("Invalid amount\n");
//         return 0.0f;
//     }

// }
// float withdraw(float balance){
//     float amount =0.0f;

//     printf("how much do you want to withdraw: $");
//     scanf("%f", &amount);

//     if (amount>0 && amount<=balance){
//         printf("successfully withdrew $%.2f\n", amount);
//         return amount;
//     }
//     else {
//         printf("Invalid amount\n");
//         return 0.0f;
//     }

// }





//  31-dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>




// int main(){


//     int scores[5] = {0};
//     int size= sizeof(scores)/sizeof(scores[0]);

//     for (int i=0; i<size; i++){
//     printf ("enter the score: ");
//     scanf ("%d", &scores[i]);
//     }
//     for (int i=0; i<size; i++){
//         printf("%d ",scores[i]);
//     }

//     return 0;
// }  
    
    
// 32-dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>




// int main(){

//     int numbers[][3]= {{1,2,3},
//                         {4,5,6},
//                         {7,8,9}};


//    for (int i=0; i<3; i++){

//        for (int j=0; j<3; j++){
//         printf("%03d ", numbers[i][j]);
    
//    } printf("\n");
//    }
    

//     return 0;
// }  
    


//  33-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>




// int main(){

//     // char fruits[][20]= {"banana", 
//     //                     "pineapple",
//     //                     "lemon"};

//     // int size = sizeof(fruits)/sizeof(fruits[0]);
    
//     // // fruits[0][0]=fruits[0][5];
//     // fruits[0][0]='c';


//     // for (int i =0 ; i<size ; i++){
//     //     printf("%s\n", fruits[i]);
//     // }

//     // EXERCISE

//     char names[3][25]={0};
//     int size = sizeof(names)/sizeof(names[0]);


//     for (int i =0 ; i<size; i++){
//     printf("Enter the name: ");
//     fgets(names[i], sizeof(names[i]), stdin);
//     names[i][strlen(names[i])-1]='\0';

//     }
//     // printf("Enter the name: ");
//     // fgets(names[0], sizeof(names[0]), stdin);
//     // names[0][strlen(names[0])-1]='\0';

//     // printf("Enter the name: ");
//     // fgets(names[1], sizeof(names[1]), stdin);
//     // names[1][strlen(names[1])-1]='\0';

//     // printf("Enter the name: ");
//     // fgets(names[2], sizeof(names[2]), stdin);
//     // names[2][strlen(names[2])-1]='\0';

//     for (int i =0 ; i<size; i++){
//     printf("%s\n",names[i] );
//     }

//     return 0;
// }  
    



// int main() {
//     char fruits[][20] = {
//         "banana",
//         "pineapple",
//         "lemon"
//     };

//     int size = sizeof(fruits) / sizeof(fruits[0]);

//     for (int i = 0; i < size; i++) {
//         for (int j = 0; fruits[i][j] != '\0'; j++) {
//             printf("%c ", fruits[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }


//  35-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// int main() {

//     // int x = 5;
//     // int y = 6;

//     // int max = (x>y) ? x : y;

//     // printf("%d", max);

//     //  2-example
    
//     // bool isnline= true;

//     // printf("%s", (isnline) ? "online": "offline");
    
    
//     //  3-example
//     int hours = 14;
//     int minutes=0;
//     char *pointer= (hours < 12)? "AM":"PM";

//     printf("%02d : %02d %s", hours, minutes,pointer);

//     return 0;
// }


//  36-dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// typedef int num;
// typedef char string[50];

// int main() {

// //     num x=3;

// //     printf("%d", x);
// // // 
// //  2-example
//     // char name[]="Jahongir";
//     // printf("%s", name);
//     // // # Jahongir'

//     string name = "jahongir";
//     printf("%s", name);

//     return 0;
// }


// 37-dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// enum day {
//     sunday =1 , monday, tuesday, wednesday , thursday , friday, saturday
// };

// int main() {

//     enum day today = saturday;

//     printf("%d", today);


//     return 0;
// }




//  38-dars

// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>


// typedef struct{
//     char name [50];
//     int age;
//     bool isfulltime;
//     float gpa ;

// }Student;

// void printstudent(Student student);

// int main() {

//     Student student1={"Jahongir", 19, true, 4.7};
//     Student student2={0};

//     strcpy(student2.name, "Rexana");
//     student2.age=18;
//     student2.isfulltime=true;
//     student2.gpa =5.0;

//     printstudent(student1);
//     printstudent(student2);

//     // printf  ("%s\n", student1.name);
//     // printf  ("%d\n", student1.age);
//     // printf  ("%.2f\n", student1.gpa);
//     // printf  ("%s\n", (student1.isfulltime)? "fulltime":"parttime");

//     // printf("\n");
    
//     // printf  ("%s\n", student2.name);
//     // printf  ("%d\n", student2.age);
//     // printf  ("%.2f\n", student2.gpa);
//     // printf  ("%s\n", (student2.isfulltime)? "fulltime":"parttime");


//     return 0;
// }

// void printstudent(Student student){
//     printf  ("Name: %s\n", student.name);
//     printf  ("age: %d\n", student.age);
//     printf  ("gpa: %.2f\n", student.gpa);
//     printf  ("he or she is: %s\n", (student.isfulltime)? "fulltime":"parttime");
//     printf("\n");
// }



//  39-dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// typedef struct{
//     char name[25];
//     int year;
//     int price;

// }Car;

// int main() {

//     // struct Car car1 = {"BMW", 2024, 30000};
//     // struct Car car2 = {"tiko", 2026, 4000};
//     // struct Car car3= {"mustang", 2024, 30000};

//     // printf("%s-%d: $%d\n", car1.name,car1.year,car1.price);
//     // printf("%s-%d: $%d\n", car2.name,car2.year,car2.price);
//     // printf("%s-%d: $%d\n", car3.name,car3.year,car3.price);
 

//     //  advanced way of arrays

//     Car cars[]={{"BMW", 2024, 30000},
//             {"tiko", 2026, 4000},
//         {"mustang", 2024, 30000}};

//     int size = sizeof(cars)/sizeof(cars[0]);

//     for (int i =0; i<size ; i++){
//         printf("%s-%d: $%d\n", cars[i].name,cars[i].year,cars[i].price);
        
//     }

   
//     return 0;
// }


//  40 - dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// void birthday(int *age);

// void changenum(int *num);

// int main() {

// //     int age = 19;
// //     int *pAge= &age;

// //     // printf("%p\n", pAge);
// //     // printf("%p", &age);
  
// //     birthday(&age);

// //     printf("you are %d years old", age);
   
// //     return 0;
// // }
// // void birthday(int *age){
// //     (*age)++;
// // }

// int x= 10;
// int *pX=&x;

// changenum(&x);

// printf("%d",x);

// }

// void changenum(int *num){
//     (*num)+=10;

// }


//  41-dars


// #include <stdio.h>
// #include <string.h>
// #include <math.h>
// #include <stdbool.h>
// #include <windows.h>
// #include <time.h>
// #include <stdlib.h>

// // int main() {

// //     FILE *pf = fopen ("output.txt", "w");

// //     if (pf==NULL){
// //         printf("Xatolik");
// //         return 1;
// //     }

// //     fprintf(pf, "hello world!!!");

// //     fclose(pf);


    

// //     FILE *pf = fopen("output.txt", "r");
// //     if (pf==NULL){
// //         printf("xatolik");
// //         return 1;
// //     }
// //     char text[1024];

// //     while (fgets(text, sizeof(text), pf )!=NULL){
// //         printf("%s", text);
// //     }
// //     fclose(pf);
// //         return 0;
// // }


// //  Chatgpt ni kodi


// int main() {

//     // 1. Faylga yozish
//     FILE *pf = fopen("output.txt", "w");

//     if (pf == NULL) {
//         printf("Xatolik: fayl ochilmadi!\n");
//         return 1;
//     }

//     fprintf(pf, "hello world!!!");

//     fclose(pf);

//     // 2. Fayldan o'qish
//     pf = fopen("output.txt", "r");

//     if (pf == NULL) {
//         printf("Xatolik: fayl ochilmadi!\n");
//         return 1;
//     }

//     char text[1024];

//     while (fgets(text, sizeof(text), pf) != NULL) {
//         printf("%s", text);
//     }

//     fclose(pf);

//     return 0;
// }

                            