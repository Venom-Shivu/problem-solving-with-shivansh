class Solution {

    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        backtrack(candidates, target, 0, new ArrayList<>());

        return result;
    }

    private void backtrack(int[] candidates,
                           int remaining,
                           int index,
                           List<Integer> current) {

        // Valid combination found
        if (remaining == 0) {

            result.add(new ArrayList<>(current));
            return;
        }

        // Invalid path
        if (remaining < 0 || index == candidates.length) {
            return;
        }

        // -----------------------------
        // Choice 1: Take current number
        // -----------------------------
        current.add(candidates[index]);

        // Stay at same index because reuse allowed
        backtrack(candidates,
                  remaining - candidates[index],
                  index,
                  current);

        // Backtrack
        current.remove(current.size() - 1);

        // -----------------------------
        // Choice 2: Skip current number
        // -----------------------------
        backtrack(candidates,
                  remaining,
                  index + 1,
                  current);
    }
}