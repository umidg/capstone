import Image from 'next/image.js';
import List from '../components/List/List.js';
// https://ui.aceternity.com/components/signup-form
export default function Home() {
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
              <label className='input input-bordered flex items-center gap-2 w-full m-2'>
                Name
                <input type='text' className='grow' placeholder='Full Name' />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2'>
                Name
                <input type='text' className='grow' placeholder='Daisy' />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2'>
                Email
                <input
                  type='text'
                  className='grow'
                  placeholder='daisy@site.com'
                />
              </label>
            </div>
            <div className='m-5 flex justify-around'>
              <label className='input input-bordered flex items-center gap-2 w-full m-2'>
                Name
                <input type='text' className='grow' placeholder='Daisy' />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2'>
                Name
                <input type='text' className='grow' placeholder='Daisy' />
              </label>
              <label className='input input-bordered flex items-center gap-2 w-full m-2'>
                Email
                <input
                  type='text'
                  className='grow'
                  placeholder='daisy@site.com'
                />
              </label>
            </div>
            <div className='m-2 flex justify-end '>
              <button className='btn btn-primary btn-outline'>Search</button>
            </div>
          </div>
        </div>
        <List />
      </div>
    </>
  );
}
