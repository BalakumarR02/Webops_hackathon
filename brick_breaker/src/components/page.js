import React, { useRef, useEffect, useState } from 'react';
import Scene from './scene';
import { registerListener } from '../utils';

const Page = () => {
  const sceneContainerRef = useRef(null);
  const [size, setSize] = useState(null);

  useEffect(() => {
    const handleResize = () => {
      const { width, height } = sceneContainerRef.current.getBoundingClientRect();
      setSize({ width, height });
    };

    const unregisterResizeListener = registerListener('resize', handleResize);

    handleResize(); // Initialize the size

    return () => {
      unregisterResizeListener(); // Cleanup the listener on unmount
    };
  }, []);

  return (
    <div className='page'>
      <div className='scene-container' ref={sceneContainerRef}>
        {size && <Scene width={size.width} height={size.height} />}
      </div>
    </div>
  );
};

export default Page;
