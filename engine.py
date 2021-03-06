from Queue import Queue

class State:
    """ State Class
    """
    def __init__(self):
        self.statemap = dict()
    
    def __init__(self, userstates):                #userstates is a dict off the states of all the users. (user->state)
        self.statemap = dict(userstates)

    def getState(self):
        """returns Statemap from user->state
        """
        return self.statemap

    def setState(self,statemap):
        self.statemap = statemap

    def setUserState(self,user,state):
        self.statemap[user]=state


class Channel:
    
    def __init__(self,label):
        self.label = label
#        self.queue = Queue()
        self.queue = []
        self.send = True

    def addToQueue(self, data):
#        self.queue.put(data)
        self.queue.append(data)

    def getFromQueue(self, state):
#        return self.queue.get()
        while not self.isEmpty():
            ret = self.queue[0]
            self.queue = self.queue[1:]
            user = ret[0]
            chkState = ret[3]
            if state.getState()[user]==chkState:
                return ret
        return None

    def getSendFlag(self):
        return self.send

    def setSendFlag(self,flag):
        self.send = flag

    def isEmpty(self):
        return len(self.queue)==0
#        return self.queue.empty()

class Channels:
    
    def __init__(self):
        self.channels = {}
    
    def getChannel(self,label):
        if not self.channels.has_key(label):
            self.channels[label] = Channel(label)
        return self.channels[label]


class Transition:

    def __init__(self, user, channel, send, state, new_state, action ):         #state,new_state = user states, send = true/false
        self.user = user
        self.channel = channel
        self.send = send
        self.initialState = state
        self.newState = new_state
        self.action = action


class Transitions:

    def __init__(self):
        self.transitions={}

    def addTransition(self,trans):            #trans is of type Transition, action is a string in this case.
        if not self.transitions.has_key(trans.user):
            self.transitions[trans.user]={}
        if not self.transitions[trans.user].has_key(trans.action):
            self.transitions[trans.user][trans.action]={}
        self.transitions[trans.user][trans.action] = [trans.initialState, trans.newState, {}, trans.channel, trans.send]

    def getTransitions(self):
        return self.transitions

    def addHookToAction(self,username, action,hook):	#hook = user->pagelet->field->perm
        if not self.transitions.has_key(username):
            return False
        if not self.transitions[username].has_key(action):
            return False

        final = self.transitions[username][action][2]
        for user in hook:
            if not final.has_key(user):
                final[user]={}
            for pagelet in hook[user]:
                if not final[user].has_key(pagelet):
                    final[user][pagelet]={}
                for field in hook[user][pagelet]:
                    final[user][pagelet][field]=hook[user][pagelet][field]
        

    def executeAction(self, user, action, state):
        if not self.transitions.has_key(user):
            return None
        if not self.transitions[user].has_key(action):
            return None
        if state.getState()[user]!=self.transitions[user][action][0]:
            return None
        return self.transitions[user][action]

    def getRecTransitions(self, user, state):
        if not self.transitions.has_key(user):
            return []
        ret = []
        for i in self.transitions[user]:
            if self.transitions[user][i][0] == state[user] and not self.transitions[user][i][4]: #only rec transitions
                ret.append(i)
        return ret

    def getUserTransitions(self, user, state):
        if not self.transitions.has_key(user):
            return []
        ret = []
        for i in self.transitions[user]:
            if self.transitions[user][i][0] == state[user] and self.transitions[user][i][4]: #only send transitions
                ret.append(i)
        return ret

        

class Field:
    
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
    
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value
    
    def getLabel(self):
        return self.label



class Fields:

    def __init__(self):
        self.fields={}

    def addField(self, field):            #field is of type Field
        self.fields[field.getLabel()]=field

    def getFields(self):
        return self.fields

    def getValueByField(self, fieldlabel):
        if not self.fields.has_key(fieldlabel):
            return None
        return self.fields[fieldlabel].getValue()

    def setValueByField(self, fieldlabel, val):
        if not self.fields.has_key(fieldlabel):
            return False
        self.fields[fieldlabel].setValue(val)
        return True

    def emptyFields(self):
        for field in self.fields:
            self.fields[field] = Field(field)




class Users:

    def __init__(self):
        self.users=[]

    def addUser(self, user):            #user is a string
        self.users.append(user)

    def getUsers(self):
        return self.users



class Pagelet:

    def __init__(self,label):
        self.label = label
        self.fields = []

    def getLabel(self):                #label is a string
        return self.label

    def addField(self, fieldLabel):            #field is of type Field
        self.fields.append(fieldLabel)

    def getFields(self):
    	return self.fields


class Pagelets:

    def __init__(self):
        self.pagelets={}

    def addPagelet(self, pagelet):
        self.pagelets[pagelet.getLabel()] = pagelet
        return pagelet
         
    def getPagelet(self, pageletlabel):
        if not self.pagelets.has_key(pageletlabel):
            return None
        return self.pagelets[pageletlabel]

    def getAllPagelets(self):        # returns a dictionary with label->pagelet
        return self.pagelets



class System:

    def __init__(self):
        self.view = {}                #view is a dictionary - user -> pageletlabel -> fieldlabel -> perm
        self.transitions = Transitions()
        self.currentState = None
        self.users = Users()
        self.pagelets = Pagelets()
        self.fields = Fields()
        self.channels = Channels()
        self.exe = {}                 #user->action->state

    def addField(self, pageletlabel, field):            #field is of type Field
        pagelet = self.pagelets.getPagelet(pageletlabel)
        if pagelet == None:
            return False
        pagelet.addField(field.getLabel())
        if self.fields.getValueByField(field.getLabel()) == None:
            self.fields.addField(field)
        return True

    def addPagelet(self, pageletlabel):
        self.pagelets.addPagelet(Pagelet(pageletlabel))

    def getPagelet(self, pageletlabel):
        return self.pagelets.getPagelet(pageletlabel)

    def getAllPagelets(self):
        return self.pagelets.getAllPagelets()

    def addUser(self, user):
        self.users.addUser(user)
        self.view[user]={}

    def getUsers(self):
        return self.users.getUsers()

    def setInitialState(self, state):        #state is of type State
        self.setCurrentState(state)

    def getCurrentState(self):
        return self.currentState

    def setCurrentState(self, state):
        self.currentState = State({})
        for user in self.getUsers():
            self.setUserCurrentState(user, state.getState()[user])

    def setUserCurrentState(self, user, state):
        self.currentState.setUserState(user, state)
        act = self.transitions.getRecTransitions(user, self.currentState.getState())
        for i in act:
            self.executeAction(user, i)


    def addFieldToView(self,user, pageletlabel, fieldlabel,perm):    #perm IN ['--', 'r-', 'rw', '-w']
        if not self.view.has_key(user):
            self.view[user]={}
        if not self.view[user].has_key(pageletlabel):
            self.view[user][pageletlabel] = {}
        self.view[user][pageletlabel][fieldlabel]=perm

    def updateFieldView(self,user,pageletlabel,fieldlabel,perm):    #perm IN ['--', 'r-', 'rw', '-w']
        if not self.view.has_key(user):
            self.view[user]={}
        if not self.view[user].has_key(pageletlabel):
            self.view[user][pageletlabel] = {}
        if perm == '--':
            if self.view[user][pageletlabel].has_key(fieldlabel):
                del self.view[user][pageletlabel][fieldlabel]
        else:
            self.view[user][pageletlabel][fieldlabel]=perm

    def getPermissions(self,user,pageletlabel,fieldlabel):
        if not self.view.has_key(user):
            return '--'
        if not self.view[user].has_key(pageletlabel):
            return '--'
        if not self.view[user][pageletlabel].has_key(fieldlabel):
            return '--'
        return self.view[user][pageletlabel][fieldlabel]
  
    def executeAction(self, user, action):
        temp = self.transitions.executeAction( user, action, self.getCurrentState())
        if temp==None:
            return False
        channel = self.channels.getChannel(temp[3])
        if temp[4]:
            self.setUserCurrentState(user, None)

        if channel.isEmpty():
            channel.addToQueue([user, temp[1],temp[2],temp[0]])
            channel.setSendFlag(temp[4])
            return

        if channel.getSendFlag() == temp[4]:
            channel.addToQueue([user,temp[1],temp[2],temp[0]])
            return

        data = channel.getFromQueue(self.getCurrentState())
        if data == None:
            return False

        self.setUserCurrentState(data[0], data[1])
        self.setUserCurrentState(user, temp[1])

        for us in data[2]:
            for pagelet in data[2][us]:
                for field in data[2][us][pagelet]:
                    self.updateFieldView(us, pagelet, field, data[2][us][pagelet][field])
        
        for us in temp[2]:
            for pagelet in temp[2][us]:
                for field in temp[2][us][pagelet]:
                    self.updateFieldView(us, pagelet, field, temp[2][us][pagelet][field])
        return True

    def getFieldByUser(self,user,pageletlabel,fieldlabel):            #get value of field if the user has permission to read it. Returns None if cant be read.
        if self.getPermissions(user,pageletlabel,fieldlabel) in ["rw","r-"]:
            return self.fields.getValueByField(fieldlabel)
        else:
            return None


    def setFieldByUser(self,user,pageletlabel,fieldlabel,val):            #set value of field if the user has permission to write on it. Returns True if set, False if not.
        if self.getPermissions(user, pageletlabel, fieldlabel) in ["rw","-w"]:
            return self.fields.setValueByField(fieldlabel, val)
        else:
            return False

    def getUserContent(self,user,pageletlabel):				#returns fieldlabel->perm
        if not self.view.has_key(user):
            return {}
        if not self.view[user].has_key(pageletlabel):
            return {}
        dic = dict(self.view[user][pageletlabel])

        if self.getCurrentState().getState()[user] == None:
            for i in dic:
                if dic[i]=='rw':
                    dic[i] = 'r-'
                if dic[i]=='-w':
                    dic[i] = '--'
        
        return dic
    
    def addTransition(self,trans):            #trans is of type Transition.
        self.transitions.addTransition(trans)
    
    def getTransitions(self):
        return self.transitions.getTransitions()

    def addHookToAction(self,user,action,hook):
        self.transitions.addHookToAction(user,action,hook)

    def getExec(self,user):
        state = self.currentState.getState()
        return self.transitions.getUserTransitions(user, state)

    def emptyFields(self):
        self.fields.emptyFields()


