import React from 'react'
import { useSelector } from 'react-redux'


export default function DashProfile() {
  const { currentUser } = useSelector(state => state.user);
  return (
    <div>
      <h1 className='font-bold text-2xl'>Your Profile</h1>
      <hr />
      <div className='p-3 bg-blue-400 rounded-lg text-white'>
        <h2><b>Name: </b> {currentUser.user.full_name}</h2>
      </div>
    </div>
  )
}
