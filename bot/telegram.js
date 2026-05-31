const axios = require("axios");

async function sendSignal(signal) {

    const message = `
🔔 OTC SIGNAL

📊 Pair: ${signal.pair}
📈 Direction: ${signal.direction}
⏳ Timeframe: ${signal.timeframe}
📊 Score: ${signal.score}
🌍 Session: ${signal.session}
`;

    const url = `https://api.telegram.org/bot${process.env.TELEGRAM_BOT_TOKEN}/sendMessage`;

    await axios.post(url, {
        chat_id: process.env.TELEGRAM_CHAT_ID,
        text: message
    });
}

module.exports = { sendSignal };