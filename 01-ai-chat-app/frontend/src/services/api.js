// services/api.js
// All API calls in one place!
// Like a service layer in Angular!

const BASE_URL = "http://localhost:8000"

export const chatAPI = {

  // Load chat history
  getHistory: async (userId) => {
    const response = await fetch(
      `${BASE_URL}/chat/history/${userId}`
    )
    return response.json()
  },

  // Clear chat history
  clearHistory: async (userId) => {
    await fetch(`${BASE_URL}/chat/history/${userId}`, {
      method: "DELETE"
    })
  },

  // Send message (streaming)
  sendMessage: async (message, userId) => {
    const response = await fetch(`${BASE_URL}/chat/stream`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message,
        user_id: userId
      })
    })
    return response
  }
}