var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const existed = this.cache.has(key) && this.cache.get(key).expireAt > now;

    this.cache.set(key, {
        value,
        expireAt: now + duration
    });

    return existed;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();
    if (!this.cache.has(key)) return -1;

    const { value, expireAt } = this.cache.get(key);
    if (expireAt > now) {
        return value;
    } else {
        this.cache.delete(key);
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (const [key, { expireAt }] of this.cache.entries()) {
        if (expireAt > now) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }
    return count;
};

/**
 * Example:
 * const timeLimitedCache = new TimeLimitedCache()
 * console.log(timeLimitedCache.set(1, 42, 1000)); // false
 * console.log(timeLimitedCache.get(1)); // 42
 * console.log(timeLimitedCache.count()); // 1
 */
