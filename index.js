require("dotenv").config();
require("./server");

const { runTrade } = require("./bot/trade");

setInterval(async () => {
    try {
        await runTrade();
    } catch (err) {
        console.error("Trade loop error:", err.message);
    }
}, 5000);

setInterval(() => {
    console.log(`[HEARTBEAT] Bot alive: ${new Date().toISOString()}`);
}, 60000);
