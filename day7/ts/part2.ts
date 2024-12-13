import { promises as fs } from "fs";

const possible = async (
  result: number,
  values: number[],
  afterIdx: number,
  curr: number,
): Promise<boolean> => {
  if (afterIdx >= values.length) {
    if (curr === result) {
      return true;
    } else {
      return false;
    }
  }

  const plus = await possible(
    result,
    values,
    afterIdx + 1,
    curr + values[afterIdx],
  );
  const mult = await possible(
    result,
    values,
    afterIdx + 1,
    curr === 0 ? values[afterIdx] : curr * values[afterIdx],
  );
  const concat = await possible(
    result,
    values,
    afterIdx + 1,
    curr === 0 ? values[afterIdx] : Number(`${curr}${values[afterIdx]}`),
  );

  return plus || mult || concat;
};

const solve = async (): Promise<void> => {
  const data = await fs.readFile("./input", "utf-8");

  let ans = 0;
  const lines = data.split("\n").filter((x) => x.trim() != "");

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const arr = line.split(":");
    const result = Number(arr[0]);
    const values = arr[1]
      .trim()
      .split(" ")
      .map((x) => Number(x));
    if (await possible(result, values, 0, 0)) {
      ans += result;
    }
  }
  console.log(ans);
};

solve();
