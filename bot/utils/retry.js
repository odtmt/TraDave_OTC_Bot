async function safeRun(fn, retries = 3) {

    for (let attempt = 1; attempt <= retries; attempt++) {

        try {
            return await fn();
        }
        catch (error) {

            console.error(
                `Attempt ${attempt}/${retries} failed:`,
                error.message
            );

            if (attempt === retries) {
                throw error;
            }

            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }
}

module.exports = {
    safeRun
};
