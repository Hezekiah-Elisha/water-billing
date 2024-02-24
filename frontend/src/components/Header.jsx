import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
import { UserCircleIcon } from '@heroicons/react/24/solid';
import { signOut } from '../redux/user/userSlice';
import api from '../api';


export default function Header() {
  const { currentUser } = useSelector(state => state.user);
  const dispatch = useDispatch();
  console.log(currentUser)
  console.log(currentUser.access_token)

  const handleSignout = async () => {
    try{
      const res = await api.delete('auth/logout', {
        headers: {
          Authorization: `Bearer ${currentUser.access_token}`,
        },
      })
      dispatch(signOut());
      localStorage.removeItem('user');
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <div className='bg-blue-400 text-white'>
        <div className='flex items-center justify-between max-w-6xl mx-auto p-3'>
            <div className='font-bold text-2xl'>
                Water Billing
            </div>
            <div className='flex gap-4'>
                <Link to='/' className='p-2 hover:bg-white hover:text-blue-500 rounded-sm '>Home</Link>
                <Link to='/about' className='p-2 hover:bg-white hover:text-blue-500 rounded-sm'>About</Link>
                {currentUser ? (
                  <div className='flex flex-row'>
                    <Link to='/dashboard/profile' className='p-2 hover:bg-white hover:text-blue-500 rounded-sm'>
                      <p className='capitalize flex flex-row align-middle'> <UserCircleIcon className='h-5 w-5'/> hi {currentUser.user.username}</p>
                    </Link>
                    <Link to='/dashboard' className='p-2 hover:bg-white hover:text-blue-500 rounded-sm'>Dashboard</Link>
                    <button onClick={handleSignout} className='p-2 hover:bg-white hover:text-blue-500 rounded-sm'>Signout</button>
                  </div>
                  ): (

                    <Link to='/signin' className='p-2 hover:bg-white hover:text-blue-500 rounded-sm'>Signin</Link>
                  )
                }
                <button>Dark</button>
            </div>
        </div>
    </div>
  )
}
