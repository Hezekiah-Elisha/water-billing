import React from 'react'
import { TrashIcon } from '@heroicons/react/24/solid'
import api from '../api'


export default function DashSupervisors() {
  const [supervisors, setSupervisors] = React.useState([])
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState(null)
  React.useEffect(() => {
    const fetchSupervisor = async () => {
      try {
        setLoading(true)
        const response = await api.get('/auth/users/role/supervisors')
        setSupervisors(response.data)
        setLoading(false)
      } catch (error) {
        setError(error)
      }
    }
    fetchSupervisor()
    }, []
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>{error.message}</div>
  return (
    <div>
      <h1 className='font-bold text-2xl flex justify-between align-middle'>
        <p>Supervisors</p>
        
      </h1>
      <hr />
      <div className='grid grid-cols-3 gap-4'>
        {supervisors.map((supervisor, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg">
            <div className="px-6 py-4">
              <div className="font-bold text-xl mb-2 capitalize">{supervisor.full_name}</div>
              <p className="text-gray-700 text-base">
                {supervisor.email}
              </p>
            </div>
            <div className="px-6 pt-4 pb-2">
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{supervisor.username}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{supervisor.email}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#{supervisor.role}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
