function Quiz(questions) {
    this.questions = questions;
    this.questionIndex = 0;
}

let ans = []

let questions = [
    new Question(
        "Sizning istimangiz chiqayaptimi(ya'ni 38'C dan yuqorimi) ?",
        
        ["Ha", "Yo'q"],
        "4"
    ),
    new Question(
        "Sizni yo'tal bezovta qilayaptimi? ",
        ["Ha", "Yo'q"],
        "7"
    ),
    new Question(
        "Sizni o'zingizni xolsiz his qilayapsizmi?", 
        ["Ha", "Yo'q"],
        "1"
        ),
    new Question(
        "Sizning ko'ngliz ayniyaptimi?", 
        ["Ha", "Yo'q"],
        "2"
        ),
    new Question(
        "Siz ta'm sezish qobilyatini yo'qotdingizmi?", 
        ["Ha", "Yo'q"],
        "3"
        )
];

Quiz.prototype.getQuestionIndex = function() {
    return this.questions[this.questionIndex];
}

let ques = []
let answers = []
let id = []

let k = 0;
let j = 0;

Quiz.prototype.guess = function(answer) {
    

    answers.push(answer);

    
    this.questionIndex++;
}


Quiz.prototype.isEnded = function() {
    return this.questionIndex === this.questions.length;
}


function Question(text, choices, answer) {
    this.text = text;
    this.choices = choices;
    this.answer = answer;
}

function displayQuestion() {
    
    if(quiz.isEnded()) {
        showScores();

    }
    else {
        let questionElement = document.getElementById("question");
        questionElement.innerHTML = quiz.getQuestionIndex().text;
        let choices = quiz.getQuestionIndex().choices;
        for(let i = 0; i < choices.length; i++) {
            let choiceElement = document.getElementById("choice" + i);
            choiceElement.innerHTML = choices[i];
            guess("btn" + i, choices[i]);
        }

        showProgress();
    }

};

function guess(id, guess) {
    let button = document.getElementById(id);
    button.onclick = function() {
        quiz.guess(guess);
        displayQuestion();
    }
};


function showProgress() {
    let currentQuestionNumber = quiz.questionIndex + 1;
};

function showScores() {
    // for(let i = 0; i < ans.length; i++){
    //     console.log(ans[i] + " ")
    // }
    for(let i = 0; i < questions.length; i++){
        ques.push(questions[i].text);
        id.push(questions[i].answer);
    }
    for(let i = 0; i < questions.length * 2; i++){
        if(i % 2 == 0){
            ans.push(id[k]);
            k++;
        } else{
            ans.push(answers[j]);
            j++;
        }
    }

    let m = 1;
    let cnt_yes = 0;
    let cnt_no = 0;
    for(let i = 1; i < ans.length; i+=2){
        if(ans[i] == "Ha"){
            cnt_yes++;
        } else {
            cnt_no++;
        }
    }

    let diagnos = "";
    if(cnt_yes == ans.length / 2){
        diagnos = "covid";
    } else if(cnt_no == ans.length / 2){
        diagnos = "sog'lom"
    } else{
        diagnos = "shamollash";
    }
    console.log(ans)

    let quizEndHTML = 
    `
    <h4 class="success-txt">Siz so'rovnomani muvaffaqiyatli yakuladingiz</h4>
    
    <h5 id='score'> Sizning tashxis: ${diagnos}</h5>

    <a href="../pages/profile.html" class="btn form__button mt-5" value="Profile">Profile</a>
    
    `;
    let quizElement = document.getElementById("quiz");
    quizElement.innerHTML = quizEndHTML;

};



// questions.forEach((answer) => {
//     console.log(answer.choice);
//     let quizAnswers = document.getElementById("quiz-answers");
//     // quizAnswers.innerHTML = questions.text;
// })

let quiz = new Quiz(questions);
displayQuestion();

