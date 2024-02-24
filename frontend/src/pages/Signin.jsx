import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { signInStart, signInSuccess, signInFailure } from '../redux/user/userSlice'
import { useDispatch, useSelector } from 'react-redux'
import api from '../api'


export default function Signin() {

  const [formData, setFormData] = useState({})
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { loading, error } = useSelector(state => state.user)

  const handleChange = async (e) => {
    setFormData({ ...formData, [e.target.id]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      dispatch(signInStart())
      const res = await api.post('/auth/login', formData)
      if (res.status === 200) {
        dispatch(signInSuccess(res.data))
        navigate('/dashboard')
      } else {
        dispatch(signInFailure(res.data))
      }
    } catch (err) {
      dispatch(signInFailure(err))
    }
    
  }

  return (
    <div className="p-3 max-w-lg mx-auto">
      <h1 className="text-3xl text-center font-semibold my-7">Sign In</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input type="email" placeholder="email" id="email" onChange={handleChange} className="bg-slate-100 p-3 rounded-lg" />
        <input type="password" placeholder="Password" id="password" onChange={handleChange} className="bg-slate-100 p-3 rounded-lg focus:border-blue-400" />
        <button className="bg-blue-400 text-white p-3 rounded-lg uppercase hover:opacity-95 disabled:opacity-55 focus:border-blue-400">
          {loading ? 'Loading...' : 'Sign In'}
        </button>
      </form>
      <div className='flex gap-2 mt-5'>
        <p>Don&apos;t have an account?</p>
        <Link to="/sign-up" className="text-slate-700 font-semibold hover:underline hover:text-blue-400">
          <span className='text-blue-500'>
            Contact Admin
          </span>
        </Link>
      </div>
      <p className="text-red-500 mt-5">
        {error ? error.message : 'Something Went Wrong!'}
      </p>
    </div>
  )
}
