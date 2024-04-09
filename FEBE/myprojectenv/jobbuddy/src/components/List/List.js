// List.js
'use client';

import { useState } from 'react';

export default function List() {
  const jobs = [
    {
      id: 1,
      title: 'Software Developer',
      description: 'Responsible for developing applications...',
    },
    {
      id: 2,
      title: 'Product Manager',
      description: 'Oversees the development and marketing strategy...',
    },
    // Add more jobs as needed
  ];
  const [selectedJobDescription, setSelectedJobDescription] = useState('');
  return (
    <>
      <div className='flex h-screen'>
        <div className='w-1/4 bg-gray-200 p-4 overflow-auto'>
          <ul>
            {jobs.map((job) => (
              <li
                key={job.id}
                className='cursor-pointer hover:bg-gray-300 p-2'
                onClick={() => setSelectedJobDescription(job.description)}
              >
                {job.title}
              </li>
            ))}
          </ul>
        </div>
        <div className='w-3/4 bg-white p-4 overflow-auto'>
          <p>
            {selectedJobDescription ||
              'Select a job title to view its description.'}
          </p>
        </div>
      </div>
    </>
  );
}
