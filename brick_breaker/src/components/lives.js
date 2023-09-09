import React from 'react';
import { getRange } from '../utils';

const Lives = ({ lives, containerWidth, unit }) => {
  const heartSize = unit * 1.5;

  return (
    <>
      {getRange(lives).map((i) => (
        <svg
          key={i}
          className='life'
          width={heartSize}
          height={heartSize}
          x={containerWidth - unit - heartSize * (i + 1) - (unit / 2) * i}
          y={unit}
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill="#FF0000" // Heart color
            d="M12 21.35l-1.45-1.32C5.4 16.18 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 7.68-8.55 11.54L12 21.35z"
          />
        </svg>
      ))}
    </>
  );
};

export default Lives;
