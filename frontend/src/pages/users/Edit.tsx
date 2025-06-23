import React, { useState } from 'react'
import MainLayout from '../../layouts/MainLayout'

const EditUserPage = () => {
  const [formData, setFormData] = useState({
    name: 'John Doe',
    email: 'john@example.com',
    role: 'admin',
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('Saving user:', formData)
  }

  return (
    <MainLayout title="Edit User">
      <div className="max-w-3xl mx-auto mt-10 bg-white dark:bg-slate-800 p-6 rounded-xl shadow">
        <h2 className="text-xl font-bold mb-4 text-slate-800 dark:text-slate-100">Edit User</h2>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-slate-700 dark:text-slate-300">Name</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="mt-1 block w-full border border-slate-300 rounded-md shadow-sm p-2 focus:ring focus:ring-indigo-300 dark:bg-slate-700 dark:border-slate-600 dark:text-white"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 dark:text-slate-300">Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="mt-1 block w-full border border-slate-300 rounded-md shadow-sm p-2 focus:ring focus:ring-indigo-300 dark:bg-slate-700 dark:border-slate-600 dark:text-white"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 dark:text-slate-300">Role</label>
            <select
              name="role"
              value={formData.role}
              onChange={handleChange}
              className="mt-1 block w-full border border-slate-300 rounded-md shadow-sm p-2 dark:bg-slate-700 dark:border-slate-600 dark:text-white"
            >
              <option value="admin">Admin</option>
              <option value="user">User</option>
              <option value="viewer">Viewer</option>
            </select>
          </div>

          <div className="text-right">
            <button
              type="submit"
              className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 px-4 rounded"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </MainLayout>
  )
}

export default EditUserPage
