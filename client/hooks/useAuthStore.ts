import { create } from 'zustand';

type AuthState = { accessToken: string | null; setAccessToken: (value: string | null) => void };

export const useAuthStore = create<AuthState>((set) => ({
  accessToken: null,
  setAccessToken: (value) => set({ accessToken: value }),
}));
