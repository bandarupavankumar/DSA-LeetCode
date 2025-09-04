/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return Promise.race([
            fn(...args), 
            new Promise((_, reject) => setTimeout(() => reject("Time Limit Exceeded"), t))
        ]);
    };
};

// Example usage:
const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);

limited(150).catch(console.log); // "Time Limit Exceeded"
limited(50).then(() => console.log("Completed in time")); // "Completed in time"
