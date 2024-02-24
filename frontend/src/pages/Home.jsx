import React from 'react'

export default function Home() {
  return (
    // info about a water billing system
    <div className='p-3 max-w-lg mx-auto'>
      <h1 className='text-3xl text-center font-semibold my-7'>Water Billing System</h1>
      <p className='text-justify'>
        This is a water billing system that allows the admin to create zones and assign supervisors to each zone.
        The supervisors are then able to add customers to their zones and generate bills for them.
      </p>
      <p className='text-justify'>
        The customers are then able to login and view their bills and pay for them.
      </p>
    </div>
  )
}
