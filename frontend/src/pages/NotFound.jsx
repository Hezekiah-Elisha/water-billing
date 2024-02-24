import React from 'react'
import NotFoundImg from '../assets/NotFoundImg.svg'

export default function NotFound() {
  return (
    <div>
        <img src={NotFoundImg} alt="Fuck" className='m-auto w-80 min-h-80' />
        <h2 className='text-center font-bold text-4xl'>Page not found</h2>
    </div>
  )
}
