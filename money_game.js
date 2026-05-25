let money = 10;
let countdown = 30;

function updateUI() {
        document.getElementById("timer").textContent =
                `Time left: ${countdown}`;
        document.getElementById("money").textContent =
                `Money: ${Math.round(money * 100) / 100}`;
}

function tick() {
        if (document.getElementById("leftButton").disabled) {
                return;
        }

        countdown--;
        if (countdown <= 0) {
                document.getElementById("startButton").disabled = false;
                document.getElementById("leftButton").disabled = true;
                document.getElementById("rightButton").disabled = true;
        }
        updateUI();
}

function fillButtonsHelper(num1) {
        let multiplier;
        if (num1 <= 0.3) {
                multiplier = 0.3;
        } else if (num1 > 0.3 && num1 <= 0.7) {
                multiplier = 0.6;
        } else {
                multiplier = 1;
        }

        // this number defines whether we will have an addition, multiplication
        let num2 = Math.random();
        if (num2 < 0.5) {
                return `+ ${Math.floor(Math.random() * money * multiplier)}`;
        }
        return `x ${(Math.floor(Math.random() * multiplier * 20) + 1) / 20 + 1}`;
}

function fillButtons() {
        // this number defines how large of an increase it will be
        let num1 = Math.random();
        document.getElementById("leftButton").textContent =
                fillButtonsHelper(num1);
        document.getElementById("rightButton").textContent =
                fillButtonsHelper(num1);
}

function addMoney(buttonName) {
        return () => {
                let leftVal = document.getElementById("leftButton").textContent;
                let rightVal =
                        document.getElementById("rightButton").textContent;
                let leftAmount;
                let rightAmount;

                switch (leftVal[0]) {
                        case "+":
                                leftAmount = money + Number(leftVal.slice(2));
                                console.log(1);
                                break;
                        case "x":
                                leftAmount = money * Number(leftVal.slice(2));
                                console.log(2);
                                break;
                }

                switch (rightVal[0]) {
                        case "+":
                                rightAmount = money + Number(rightVal.slice(2));
                                console.log(3);
                                break;
                        case "x":
                                rightAmount = money * Number(rightVal.slice(2));
                                console.log(4);
                                break;
                }

                if (buttonName == "leftButton" && leftAmount >= rightAmount) {
                        money = leftAmount;
                } else if (
                        buttonName == "rightButton" &&
                        rightAmount >= leftAmount
                ) {
                        money = rightAmount;
                } else {
                        console.log("Oof, you got it wrong");
                }

                fillButtons();
                updateUI();
        };
}

function onStart() {
        document.getElementById("leftButton").disabled = false;
        document.getElementById("rightButton").disabled = false;
        document.getElementById("leftButton").addEventListener(
                "click",
                addMoney("leftButton"),
        );
        document.getElementById("rightButton").addEventListener(
                "click",
                addMoney("rightButton"),
        );
        fillButtons();
        setInterval(tick, 1000);
        document.getElementById("startButton").disabled = true;
}

document.getElementById("startButton").addEventListener("click", onStart);
