// List.js
'use client';

import axios from 'axios';
import { useEffect, useState } from 'react';

export default function List(props) {
  const setUrl = 'http://127.0.0.1:5001';
  console.log(props.jobs, 'props');
  // const jobs = [
  //   {
  //     'Company Name': [['W Ralston']],
  //     'Job Description': ['Account ManagerInteplast Group '],
  //     'Job Location': ['Remote'],
  //     'Job Title': [
  //       ['Account Manager (Quebec) / Sales Account Manager (Quebec)'],
  //     ],
  //     'Job Type': ['Permanent'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/kBVparJ2RU7Sm2Gs1evW4Mw936cGPkHr9hk3S-WF6FjQKzZth-1drg',
  //     ],
  //     Qualifications: [
  //       'Microsoft Powerpoint, Microsoft Word, Microsoft Excel, Microsoft Outlook, Sales, Customer service, Post-secondary education, Outside sales, English, Inside sales, AS400, Driving License',
  //     ],
  //     Salary: ['Estimated: $64.5K\u2013$81.7K a year'],
  //   },
  //   {
  //     'Company Name': [['BDO Recruitment Services - Canada - 5.0']],
  //     'Job Description': ['Nicol Insurance is a '],
  //     'Job Location': ['Kincardine, ON'],
  //     'Job Title': [['Personal Lines - Account Manager']],
  //     'Job Type': ['Full-time'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/hNohf_AqK6q8xJ4o9tmwbU206TMEAu_95POdBGYdVR21a13e_XW2Cg',
  //     ],
  //     Qualifications: [
  //       'RIBO License, Organizational skills, Computer skills, Communication skills',
  //     ],
  //     Salary: ['Estimated: $54.4K\u2013$68.9K a year'],
  //   },
  //   {
  //     'Company Name': [['ArcelorMittal Tubular Products Woodstock - 3.9']],
  //     'Job Description': ['Hellow Job description'],
  //     'Job Location': ['Woodstock, ON'],
  //     'Job Title': [['Sales Account Manager']],
  //     'Job Type': ['Full-time'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/dNkRsD_uBP6kdUL_7Ip_xQ9Emhe2JGBngHGWci4aT8ZujYjF21d8hw',
  //     ],
  //     Qualifications: [
  //       'Microsoft Word, Microsoft Excel, Microsoft Outlook, Post-secondary education, Visio, Analysis skills, Business planning, Manufacturing, Communication skills, Time management',
  //     ],
  //     Salary: ['Estimated: $77.8K\u2013$98.5K a year'],
  //   },
  //   {
  //     'Company Name': [['Uline - 3.1']],
  //     'Job Description': ['Regina'],
  //     'Job Location': ['Regina, SK'],
  //     'Job Title': [['Sales Account Manager']],
  //     'Job Type': ['Full-time'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/Liggrbh8Qatd8azGKHjG9cQXUJyI59k0kMjG9aymoUJlpE8EaBlyQw',
  //     ],
  //     Qualifications: [
  //       "Sales, High school diploma or GED, Presentation skills, Bachelor's, Communication skills, Driving Licence",
  //     ],
  //     Salary: ['$125,000\u2013$150,000 a year'],
  //   },
  //   {
  //     'Company Name': [['Uline - 3.1']],
  //     'Job Description': ['Hello Job description'],
  //     'Job Location': ['Moose Jaw, SK'],
  //     'Job Title': [['Sales Account Manager']],
  //     'Job Type': ['Full-time'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/HCVVHTnXksjucqGQRX41E-1UHqGyon3aq60OgActYIa7KdF6xEOE1A',
  //     ],
  //     Qualifications: [
  //       "Sales, High school diploma or GED, Presentation skills, Bachelor's, Communication skills, Driving Licence",
  //     ],
  //     Salary: ['$125,000\u2013$150,000 a year'],
  //   },
  //   {
  //     'Company Name': [['ZeroKey']],
  //     'Job Description': ['Hellow Description'],
  //     'Job Location': ['Calgary, AB'],
  //     'Job Title': [['Senior Account Manager']],
  //     'Job Type': ['Permanent | Full-time'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/YD-wy5GHwqMHKqkCl3ZIx4hV_vIIej11rtxbRmoxWDJ8Gr_3YyDPOw',
  //     ],
  //     Qualifications: [
  //       "Microsoft Word, Microsoft Excel, Microsoft Outlook, Sales, Customer service, Engineering, Windows, Schedule management, Project management, Presentation skills, Bachelor's, B2B sales, Organizational skills, Enterprise sales, HubSpot, Communication skills",
  //     ],
  //     Salary: ['$50,000\u2013$150,000 a year'],
  //   },
  //   {
  //     'Company Name': [['ClaimSecure - 2.3']],
  //     'Job Description': ['Reporting to the Director'],
  //     'Job Location': ['Mississauga, ON'],
  //     'Job Title': [['Account Manager - Remote']],
  //     'Job Type': ['Permanent | Full-time'],
  //     'Job URL': [
  //       'https://www.simplyhired.ca/job/AwTGf6gbSojztvfyik8GaAXUiVWIrB546O3SdE8PUAa4gzxjjkIxVA',
  //     ],
  //     Qualifications: [
  //       "Microsoft Powerpoint, Microsoft Word, Microsoft Excel, Microsoft Outlook, Sales, Customer service, Presentation skills, Bachelor's, Customer relationship management, Organizational skills, College diploma, Leadership, Communication skills, Negotiation, Driving License, etc, Time management",
  //     ],
  //     Salary: ['$65,000\u2013$70,000 a year'],
  //   },
  //   {
  //     'Big Bigrams': [
  //       [
  //         [
  //           'personal lines',
  //           'account executive',
  //           'account manager',
  //           'client worried',
  //           'daily downloaded',
  //           'account lines',
  //           'member management',
  //           'nicol insurance',
  //           'team member',
  //           'multitasknpossess capability',
  //         ],
  //         [
  //           'new business',
  //           'north american',
  //           'business opportunities',
  //           'american automotive',
  //           'arcelormittal tubular',
  //           'business plan',
  //           'commercial issues',
  //           'current potential',
  //           'manufacturing experience',
  //           'knowledge experience',
  //         ],
  //         [
  //           'new markets',
  //           'quality products',
  //           'account manager',
  //           'account managernpay',
  //           'accounts bring',
  //           'accounts industries',
  //           'allowance nmileage',
  //           'alongside peers',
  //           'americas leading',
  //           'annual onsite',
  //         ],
  //         [
  //           'new markets',
  //           'quality products',
  //           'account manager',
  //           'account managernpay',
  //           'accounts bring',
  //           'accounts industries',
  //           'allowance nmileage',
  //           'alongside peers',
  //           'americas leading',
  //           'annual onsite',
  //         ],
  //         [
  //           'dirty process',
  //           'account manager',
  //           'sr account',
  //           'dirty champion',
  //           'location technology',
  //           'responsible manager',
  //           'operational visibility',
  //           'precisely digitizing',
  //           'process sr',
  //           'quantum rtls',
  //         ],
  //         [
  //           'ability think',
  //           'responsive addition',
  //           'handle escalated',
  //           'high level',
  //           'product services',
  //           'skills ability',
  //           'skills strong',
  //           'ability deliver',
  //           'ability function',
  //           'ability initiative',
  //         ],
  //         [
  //           'cross functional',
  //           'existing new',
  //           'new opportunities',
  //           'value proposition',
  //           'year future',
  //           'ability build',
  //           'ability create',
  //           'ability work',
  //           'account management',
  //           'account manager',
  //         ],
  //         [
  //           'account manager',
  //           'cross border',
  //           'order ensure',
  //           'senior account',
  //           'speedy transport',
  //           'transport group',
  //           'able perform',
  //           'current accounts',
  //           'develop accounts',
  //           'accounts identify',
  //         ],
  //         [
  //           'internal customers',
  //           'account support',
  //           'customer service',
  //           'highly preferred',
  //           'hobart canada',
  //           'key account',
  //           'making decisions',
  //           'organization service',
  //           'service programs',
  //           'specialist support',
  //         ],
  //       ],
  //     ],
  //   },
  // ];
  const [selectedJob, setSelectedJob] = useState(null);

  const [activeTab, setActiveTab] = useState('free');

  const [allJobs, setAllJobs] = useState(null);
  const [personal, setDetails] = useState(null);

  const [coverLetterFree, setCoverLetterFree] = useState('');
  const [coverLetterPremium, setCoverLetterPremium] = useState('');

  const coverLetterModal = () => {
    document.getElementById('my_modal_4').showModal();
  };

  const getCoverLetterFree = async ({ company, job_title, qualifications }) => {
    setCoverLetterFree(null);
    await axios
      .post(setUrl + '/api/cover_letter_free', {
        ...personal,
        job_title,
        bigrams:
          allJobs[allJobs.length - 1]?.['Important Bigrams']?.[0]?.[
            selectedJob
          ].join(','),
        qualifications,
        company,
      })
      .then((d) => setCoverLetterFree(d?.data?.cover_letter))
      .catch((e) => console.log(e));
  };

  const getCoverLetterPremium = async ({
    company,
    job_title,
    qualifications,
  }) => {
    setCoverLetterPremium(null);
    await axios
      .post(setUrl + '/api/cover_letter_premium', {
        ...personal,
        job_title,
        bigrams:
          allJobs[allJobs.length - 1]?.['Important Bigrams']?.[0]?.[
            selectedJob
          ].join(','),
        qualifications,
        company,
      })
      .then((d) => setCoverLetterPremium(d?.data?.cover_letter))
      .catch((e) => console.log(e));
  };

  useEffect(() => {
    setAllJobs(props.jobs);
    setDetails(props.personal);
  }, [props]);

  return (
    <>
      <div className='flex h-screen'>
        <div className='w-1/4 bg-gray-200 p-4 overflow-auto'>
          <ul>
            {allJobs
              ? allJobs.map((job, i) => (
                  <li
                    key={job.id}
                    className={`cursor-pointer hover:bg-gray-300 p-2 py-10 ${
                      i == 0 ? 'bg-slate-400' : ''
                    }`}
                    onClick={() => {
                      // console.log(job['Job Description']?.[0]);
                      // setSelectedJobDescription(job['Job Description']?.[0]);
                      setSelectedJob(i);
                    }}
                  >
                    {job['Job Title']?.[0]?.[0]}
                  </li>
                ))
              : 'No Jobs'}
          </ul>
        </div>
        <div className='w-3/4 bg-white p-4 overflow-auto whitespace-pre-wrap'>
          {selectedJob != null ? (
            <div>
              <p className=' font-extrabold  text-xl'>
                {allJobs[selectedJob]?.['Company Name']?.[0]?.[0]}
              </p>
              <p className='font-semibold text-3xl'>
                {allJobs[selectedJob]?.['Job Title']?.[0]}
              </p>
              <p className=' italic'>
                {allJobs[selectedJob]?.['Job Location']?.[0]}
              </p>
              <p className=' underline'>
                {allJobs[selectedJob]?.['Job Type']?.[0]}
              </p>
              <p className=' font-normal'>
                Salary: {allJobs[selectedJob]?.['Salary']?.[0]}
              </p>
              <br />
              <p className=' italic font-2xl'>
                <span className=' font-bold not-italic'>Qualifications: </span>
                {allJobs[selectedJob]?.['Qualifications']?.[0]}
              </p>
              <br />
              <p>{allJobs[selectedJob]?.['Job Description']?.[0]}</p>
              <button
                className='btn btn-primary btn-fill text-white'
                onClick={() => coverLetterModal()}
              >
                Generate
              </button>
            </div>
          ) : (
            'Select a job title to view its description.'
          )}
        </div>
      </div>

      <dialog id='my_modal_4' className='modal'>
        <div className='modal-box w-11/12 max-w-5xl'>
          <div role='tablist' className='tabs tabs-lifted w-full'>
            <div
              className={`tab w-max  ${
                activeTab === 'free' ? 'tab-active' : ''
              }`}
              onClick={() => {
                getCoverLetterFree({
                  company: allJobs?.[selectedJob]?.['Company Name']?.[0]?.[0],
                  job_title: allJobs?.[selectedJob]?.['Job Title']?.[0]?.[0],
                  qualifications:
                    allJobs?.[selectedJob]?.['Qualifications']?.[0],
                });
                setActiveTab('free');
              }}
            >
              Free Cover Letter
            </div>
            <div
              role='tabpanel'
              className={`tab-content bg-base-100 border-base-300 rounded-box p-6 ${
                activeTab === 'free' ? '' : 'hidden'
              }`}
            >
              <p className=''>
                {coverLetterFree
                  ? coverLetterFree
                  : 'Please Wait! Creating cover letter...'}
              </p>
            </div>

            <div
              className={`tab w-max ${
                activeTab === 'premium' ? 'tab-active' : ''
              }`}
              onClick={() => {
                getCoverLetterPremium({
                  company: allJobs?.[selectedJob]?.['Company Name']?.[0]?.[0],
                  job_title: allJobs?.[selectedJob]?.['Job Title']?.[0]?.[0],
                  qualifications:
                    allJobs?.[selectedJob]?.['Qualifications']?.[0],
                });
                setActiveTab('premium');
              }}
            >
              Premium Cover Letter
            </div>
            <div
              role='tabpanel'
              className={`tab-content bg-base-100 border-base-300 rounded-box p-6 ${
                activeTab === 'premium' ? '' : 'hidden'
              }`}
            >
              <p className=''>
                {coverLetterPremium
                  ? coverLetterPremium
                  : 'Please Wait! Creating cover letter...'}
              </p>
            </div>
          </div>
          <div className='modal-action'>
            <form method='dialog'>
              <button className='btn'>Close</button>
            </form>
          </div>
        </div>
      </dialog>
    </>
  );
}
