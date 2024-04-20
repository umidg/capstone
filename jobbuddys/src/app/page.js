'use client';
import Image from 'next/image.js';
import List from '../components/List/List.js';
import { useEffect, useState } from 'react';
import axios from 'axios';
// https://ui.aceternity.com/components/signup-form
export default function Home() {
  const setUrl = 'http://127.0.0.1:5001';

  const [data, setData] = useState({
    full_name: 'Umid Ghimire',
    skills: 'management, finance, account',
    education: 'Bachelors in Engineering, PG in AIML',
    experience: '5 years of exoeirnce in acounting and finance',
    job_title: 'Account Manager',
    category: 'Manager',
  });

  const [jobs, setJobs] = useState(null);

  useEffect(() => {}, []);

  const search = async () => {
    await axios
      .post(setUrl + '/api/jobs', { job_title: data.job_title })
      .then((d) => d && setJobs(d.data))
      .catch((e) => console.log(e));
  };

  return (
    <>
      <div className='navbar bg-base-100'>
        <div className='flex-1'>
          <a className='btn btn-ghost text-xl'>Job Buddy</a>
        </div>
        <div className='flex-none gap-2'>
          <input
            type='checkbox'
            value='synthwave'
            className='toggle theme-controller'
          />
          {/* <div className='form-control'>
            <input
              type='text'
              placeholder='Search'
              className='input input-bordered w-24 md:w-auto'
            />
          </div> */}
          <div className='dropdown dropdown-end'>
            <div
              tabIndex={0}
              role='button'
              className='btn btn-ghost btn-circle avatar'
            >
              <div className='w-10 rounded-full'>
                <img
                  alt='Tailwind CSS Navbar component'
                  src='https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg'
                />
              </div>
            </div>
            <ul
              tabIndex={0}
              className='mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52'
            >
              <li>
                <a className='justify-between'>
                  Profile
                  <span className='badge'>New</span>
                </a>
              </li>
              <li>
                <a>Settings</a>
              </li>
              <li>
                <a>Logout</a>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className='flex flex-col w-full border-opacity-50'>
        <div className='grid card bg-base-300 rounded-box place-items-center pt-5 '>
          <div className='mt-24'>
            <p className=' text-center font-bold text-4xl mb-5'>
              Unlock Your Dream Job: Instant, Personalized Cover Letters
            </p>

            <p className='text-center text-xl mb-24'>
              Discover Your Ideal Job and Generate a Winning Cover Letter in
              Seconds with Our AI-Powered Tool
            </p>
          </div>
          <div className=''>
            <div className='m-5 flex justify-around'>
              <label className='input input-bordered flex items-center gap-2 w-full m-2 bg-white'>
                Name
                <input
                  type='text'
                  className='grow'
                  placeholder='Full Name'
                  value={data.full_name}
                  onChange={(e) =>
                    setData({ ...data, full_name: e.target.value })
                  }
                />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2 bg-white'>
                Skills
                <input
                  type='text'
                  className='grow'
                  placeholder='Enter with commas'
                  value={data.skills}
                  onChange={(e) => setData({ ...data, skills: e.target.value })}
                />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2 bg-white'>
                Experience
                <input
                  type='text'
                  className='grow'
                  placeholder='Experience'
                  value={data.experience}
                  onChange={(e) =>
                    setData({ ...data, experience: e.target.value })
                  }
                />
              </label>
            </div>
            <div className='m-5 flex justify-around'>
              <label className='input input-bordered flex items-center gap-2 w-full m-2 bg-white'>
                Education
                <input
                  type='text'
                  className='grow'
                  placeholder='Education'
                  value={data.education}
                  onChange={(e) =>
                    setData({ ...data, education: e.target.value })
                  }
                />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2 bg-white'>
                Job Title
                <input
                  type='text'
                  className='grow'
                  placeholder='Account Manger, Customer Service'
                  value={data.job_title}
                  onChange={(e) =>
                    setData({ ...data, job_title: e.target.value })
                  }
                />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2 bg-white'>
                Category
                <input
                  type='text'
                  className='grow'
                  placeholder='Manager, Scientist, Developer...'
                  value={data.category}
                  onChange={(e) =>
                    setData({ ...data, category: e.target.value })
                  }
                />
              </label>
            </div>
            <div className='m-2 flex justify-end '>
              <button
                className='btn btn-primary btn-outline'
                onClick={() => search(data)}
              >
                Search
              </button>
            </div>
          </div>
        </div>
        <List jobs={jobs} personal={data} />
      </div>
    </>
  );
}
