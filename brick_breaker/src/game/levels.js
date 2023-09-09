import { getRange } from '../utils';

export const BLOCK_MAX_DENSITY = 3;

const getRandomBlock = () => Math.floor(Math.random() * BLOCK_MAX_DENSITY);

// Function to generate blocks for a level
const generateBlocks = (rows, columns, densityMultiplier) => {
  return getRange(rows).map(() =>
    getRange(columns).map(() => getRandomBlock() * densityMultiplier)
  );
};

// Define difficulty levels
const createLevel = (lives, paddleWidth, speed, rows, columns, densityMultiplier) => ({
  lives,
  paddleWidth,
  speed,
  blocks: generateBlocks(rows, columns, densityMultiplier),
});

export const LEVELS = [
  createLevel(5, 3.5, 1, 3, 6, 1),   // Level 1
  createLevel(4, 3, 1.4, 4, 7, 1),   // Level 2
  createLevel(3, 2.5, 1.8, 5, 8, 1), // Level 3
  createLevel(3, 2, 2.2, 6, 9, 1),   // Level 4
  // Add more levels with different configurations here
];
