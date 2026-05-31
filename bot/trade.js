const { safeRun } = require("./utils/retry");
const { sendSignal } = require("./telegram");

let lastSignalTime = 0;
const COOLDOWN = process.env.COOLDOWN ? Number(process.env.COOLDOWN) : 60000;

// 🌍 POOL OF PAIRS (add/remove anytime)
const PAIRS = [
    "EURUSD-OTC",
    "GBPUSD-OTC",
    "USDJPY-OTC",
    "AUDUSD-OTC",
    "USDCHF-OTC",
    "EURGBP-OTC"
];

// pick random item from array
function pickRandom(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function tradeLogic() {

    console.log("Checking market...");

    const now = Date.now();

    if (now - lastSignalTime < COOLDOWN) {
        return null;
    }

    // 🎲 RANDOM PAIR
    const pair = pickRandom(PAIRS);

    // fake market conditions (placeholder logic)
    const rsi = Math.random() * 100;
    const trend = Math.random() > 0.5;

    let signal = null;

    if (rsi < 30 && trend) {
        signal = {
            pair,
            direction: "BUY",
            timeframe: process.env.TIMEFRAME || "5m",
            score: 80 + Math.floor(Math.random() * 10),
            session: "ACTIVE"
        };
    }

    if (rsi > 70 && !trend) {
        signal = {
            pair,
            direction: "SELL",
            timeframe: process.env.TIMEFRAME || "5m",
            score: 80 + Math.floor(Math.random() * 10),
            session: "ACTIVE"
        };
    }

    if (signal) {
        lastSignalTime = now;
    }

    return signal;
}

async function runTrade() {

    const signal = await safeRun(tradeLogic, 3);

    if (!signal) {
        console.log("No valid signal");
        return;
    }

    console.log(`📡 SIGNAL: ${signal.pair} ${signal.direction}`);

    try {
        await sendSignal(signal);
        console.log("📲 Telegram sent");
    } catch (err) {
        console.error("Telegram error:", err.message);
    }
}

module.exports = { runTrade };