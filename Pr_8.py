class stack: st = [] def isempty(self): return (len(self.st)==0) def push(self,data): self.st.append(data) def pop(self): return self.st.pop(-1) s = stack() 4

s.push(1) s.push(2) s.push(3) print(s.isempty()) print(s.pop()) print(s.pop()) print(s.pop()) print(s.isempty())
