const { safeRun } = require("./utils/retry");

async function tradeLogic() {

    console.log("Checking market...");

    await new Promise(resolve => setTimeout(resolve, 1000));

    const win = Math.random() > 0.5;

    return {
        success: true,
        result: win ? "WIN" : "LOSS"
    };
}

async function runTrade() {

    const result = await safeRun(tradeLogic, 3);

    console.log(`Trade Result: ${result.result}`);
}

module.exports = {
    runTrade
};
