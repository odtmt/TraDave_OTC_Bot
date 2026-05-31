const { safeRun } = require("./utils/retry");
const { sendSignal } = require("./telegram");

let lastSignalTime = 0;

// =======================
// ⏱️ CONFIG
// =======================
const SIGNAL_INTERVAL = 12 * 60 * 1000; // 12 minutes between signals
const ENTRY_DELAY = 2 * 60 * 1000; // signal sent 2 mins before entry
const TRADE_STEP = 3 * 60 * 1000; // martingale step = 3 mins

// =======================
// 🌍 SESSION LOGIC
// =======================
function getSession() {
    const hour = new Date().getUTCHours();

    if (hour >= 0 && hour < 7) return "ASIA";
    if (hour >= 7 && hour < 13) return "LONDON";
    if (hour >= 13 && hour < 21) return "NEW_YORK";
    return "LATE";
}

// =======================
// 🎯 PAIRS BY SESSION
// =======================
const SESSION_PAIRS = {
    ASIA: ["USDJPY-OTC", "AUDUSD-OTC", "NZDUSD-OTC"],
    LONDON: ["EURUSD-OTC", "GBPUSD-OTC", "EURGBP-OTC"],
    NEW_YORK: ["EURUSD-OTC", "GBPUSD-OTC", "USDCHF-OTC"],
    LATE: ["EURUSD-OTC"]
};

// =======================
// 🎲 HELPERS
// =======================
function pick(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// fake but structured signal logic
function generateDirection() {
    const rsi = Math.random() * 100;
    const trend = Math.random() > 0.5;

    if (rsi < 35 && trend) return "BUY";
    if (rsi > 65 && !trend) return "SELL";
    return null;
}

// =======================
// 📊 MARTINGALE BUILDER
// =======================
function buildMartingale(baseTime) {

    return [
        { level: 1, time: new Date(baseTime) }, // ENTRY
        { level: 2, time: new Date(baseTime + TRADE_STEP) },
        { level: 3, time: new Date(baseTime + TRADE_STEP * 2) },
        { level: 4, time: new Date(baseTime + TRADE_STEP * 3) }
    ];
}

// =======================
// 🧠 MAIN LOGIC
// =======================
function tradeLogic() {

    const now = Date.now();

    // ⛔ enforce 12-minute spacing
    if (now - lastSignalTime < SIGNAL_INTERVAL) {
        return null;
    }

    const session = getSession();
    const pair = pick(SESSION_PAIRS[session]);

    const direction = generateDirection();

    if (!direction) return null;

    // 🕒 ENTRY TIME = now + 2 minutes
    const entryTime = now + ENTRY_DELAY;

    lastSignalTime = now;

    return {
        pair,
        direction,
        session,
        timeframe: "3m",
        score: 75 + Math.floor(Math.random() * 20),

        // 🕒 ENTRY TIME
        entry_time: new Date(entryTime).toISOString(),

        // 📊 MARTINGALE TIMELINE (REAL TIMES)
        martingale: buildMartingale(entryTime).map(m => ({
            level: m.level,
            time: m.time.toISOString()
        })),

        // ⏰ SEND SIGNAL 2 MIN BEFORE ENTRY
        send_at: entryTime - ENTRY_DELAY
    };
}

// =======================
// 🚀 RUNNER
// =======================
async function runTrade() {

    const signal = await safeRun(tradeLogic, 3);

    if (!signal) {
        console.log("No valid signal");
        return;
    }

    const delay = signal.send_at - Date.now();

    console.log(`📡 [${signal.session}] Signal scheduled in ${Math.floor(delay / 1000)}s`);
    console.log(`📊 ${signal.pair} | ${signal.direction}`);
    console.log(`🕒 Entry: ${signal.entry_time}`);

    setTimeout(async () => {
        try {
            await sendSignal(signal);
            console.log("📲 Telegram signal sent");
        } catch (err) {
            console.error("Telegram error:", err.message);
        }
    }, Math.max(0, delay));
}

module.exports = { runTrade };