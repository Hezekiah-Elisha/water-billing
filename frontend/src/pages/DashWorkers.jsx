import React, {useState} from 'react'
import api from '../api'
import Modal from 'react-modal'

export default function DashWorkers() {
  const [workers, setWorkers] = React.useState([])
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState(null)
  const [isModalOpen, setIsModalOpen] = React.useState(false)

  const [username, setUsername] = useState('');
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission here. For example, you can call an API to create a new worker.
    console.log({ username, fullName, email, password, role });
    closeModal();
  };



  const openModal = () => {
    setIsModalOpen(true);
  };
  const closeModal = () => {
    setIsModalOpen(false);
  };

  React.useEffect(() => {
    const fetchWorkers = async () => {
      try {
        setLoading(true)
        const response = await api.get('/auth/users/role/workers')
        setWorkers(response.data)
        setLoading(false)
      } catch (error) {
        setError(error)
      }
    }
    fetchWorkers()
    }, []
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>{error.message}</div>

  return (
    <div>
      <h1 className='font-bold text-2xl flex justify-between align-middle'>
        <p>Workers</p>
        <span>
        <button onClick={openModal} className='text-sm bg-blue-400 p-2 rounded-lg text-white'>Create Worker</button>
          <Modal
            isOpen={isModalOpen}
            onRequestClose={closeModal}
            style={{
              overlay: {
                backgroundColor: 'rgba(0, 0, 0, 0.5)'
              },
              content: {
                top: '50%',
                left: '50%',
                right: 'auto',
                bottom: 'auto',
                marginRight: '-50%',
                transform: 'translate(-50%, -50%)',
              }
            }}
          >
            <form action="" className='flex flex-col gap-4'>
              <input type="text" placeholder='Username' className='bg-slate-100 p-3 rounded-lg focus:border-blue-400'/>
              <input type="text" placeholder='Full Name' className='bg-slate-100 p-3 rounded-lg focus:border-blue-400'/>
              <input type="email" placeholder='email'className='bg-slate-100 p-3 rounded-lg focus:border-blue-400'/>
              <input type="password" placeholder='password' className='bg-slate-100 p-3 rounded-lg focus:border-blue-400'/>
              <select name="" id="" className='bg-slate-100 p-3 rounded-lg focus:border-blue-400'>
                <option value="">Select Role</option>
                <option value="">Worker</option>
                <option value="">Supervisor</option>
              </select>
              <div className='flex flex-row justify-around gap-4'>
                <button className='bg-blue-400 px-4 py-8 rounded-md text-white uppercase'>send</button>
                <button className='bg-red-400 px-4 py-8 rounded-md text-white uppercase' onClick={closeModal}>Close</button>
              </div>
            </form>
          </Modal>
        </span>
      </h1>
      <hr />
      <div className='grid grid-cols-3 gap-4'>
        {workers.map((worker, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg">
            <div className="px-6 py-4">
              <div className="font-bold text-xl mb-2 capitalize">{worker.full_name}</div>
              <p className="text-gray-700 text-base">
                {worker.email}
              </p>
            </div>
            <div className="px-6 pt-4 pb-2">
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{worker.username}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{worker.email}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#{worker.role}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
