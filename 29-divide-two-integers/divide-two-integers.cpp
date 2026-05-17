class Solution {
public:

    int divide(int dividend, int divisor) {

        // Handle overflow case
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        // Use long long to avoid overflow
        long long dvd = labs(dividend);
        long long dvs = labs(divisor);

        long long quotient = 0;

        // Keep subtracting largest possible multiples
        while (dvd >= dvs) {

            long long temp = dvs;
            long long multiple = 1;

            // Double temp until it exceeds dividend
            while ((temp << 1) <= dvd) {
                temp <<= 1;
                multiple <<= 1;
            }

            // Subtract largest chunk
            dvd -= temp;

            // Add corresponding multiple
            quotient += multiple;
        }

        // Determine sign
        if ((dividend < 0) ^ (divisor < 0)) {
            quotient = -quotient;
        }

        return (int)quotient;
    }
};