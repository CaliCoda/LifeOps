import React, { useState } from 'react'

export default function FormsDemo() {
  const [value, setValue] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    alert(`Submitted: ${value}`)
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Demo Input:
        <input
          type="text"
          value={value}
          onChange={e => setValue(e.currentTarget.value)}
        />
      </label>
      <button type="submit">Submit</button>
    </form>
  )
}