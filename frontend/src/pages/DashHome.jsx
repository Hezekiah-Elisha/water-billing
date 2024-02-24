import React from 'react'
import Sample from '../assets/sample.jpg'
import { Link } from 'react-router-dom'
import { useSelector } from 'react-redux';

export default function DashHome() {
  const { currentUser } = useSelector(state => state.user);

  return (
    <div className=''>
      <div className='w-full'>
        <div className='flex flex-row justify-between items-center gap-4' >
          <Link to="/dashboard/profile" className='flex bg-blue-300 w-full p-6 gap-2 rounded-lg'>
            <img src={Sample} alt="" className='max-w-48 rounded-full object-fit w-full'/>
            <div>
              <p className='text-white text-4xl font-bold capitalize'>Welcome {currentUser.user.username}</p>
              <div className='flex flex-row'>
                <div className='flex flex-col justify-center items-center mr-4'>
                  <p className='text-xs text-gray-600'>Total Customers</p>
                  <p className='text-2xl font-bold'>1,000</p>
                </div>
                <div className='flex flex-col justify-center items-center mr-4'>
                  <p className='text-xs text-gray-600'>Total Meters</p>
                  <p className='text-2xl font-bold'>1,000</p>
                </div>
                <div className='flex flex-col justify-center items-center mr-4'>
                  <p className='text-xs text-gray-600'>Total Bills</p>
                  <p className='text-2xl font-bold'>1,000</p>
                </div>
              </div>
            </div>
          </Link>
        </div>
      </div>
      <div className='flex gap-10 mt-10'>
        <div className='bg-blue-300 rounded-lg p-8'>
          <p className='text-xs'>Number of Supervisors</p> 
          <p className='text-2xl font-bold'>50</p>         
        </div>
        <div className='bg-blue-300 rounded-lg p-8'>
          <p className='text-xs'>Number of Workers</p>
          <p className='text-2xl font-bold'>50</p>         
          
        </div>
      </div>
    </div>
  )
}
