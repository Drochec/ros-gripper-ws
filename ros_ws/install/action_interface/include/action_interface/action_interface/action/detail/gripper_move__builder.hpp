// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from action_interface:action/GripperMove.idl
// generated code does not contain a copyright notice

#ifndef ACTION_INTERFACE__ACTION__DETAIL__GRIPPER_MOVE__BUILDER_HPP_
#define ACTION_INTERFACE__ACTION__DETAIL__GRIPPER_MOVE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "action_interface/action/detail/gripper_move__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_Goal_action
{
public:
  Init_GripperMove_Goal_action()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interface::action::GripperMove_Goal action(::action_interface::action::GripperMove_Goal::_action_type arg)
  {
    msg_.action = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_Goal>()
{
  return action_interface::action::builder::Init_GripperMove_Goal_action();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_Result_complete
{
public:
  Init_GripperMove_Result_complete()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interface::action::GripperMove_Result complete(::action_interface::action::GripperMove_Result::_complete_type arg)
  {
    msg_.complete = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_Result>()
{
  return action_interface::action::builder::Init_GripperMove_Result_complete();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_Feedback_running
{
public:
  Init_GripperMove_Feedback_running()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interface::action::GripperMove_Feedback running(::action_interface::action::GripperMove_Feedback::_running_type arg)
  {
    msg_.running = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_Feedback>()
{
  return action_interface::action::builder::Init_GripperMove_Feedback_running();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_SendGoal_Request_goal
{
public:
  explicit Init_GripperMove_SendGoal_Request_goal(::action_interface::action::GripperMove_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::action_interface::action::GripperMove_SendGoal_Request goal(::action_interface::action::GripperMove_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_SendGoal_Request msg_;
};

class Init_GripperMove_SendGoal_Request_goal_id
{
public:
  Init_GripperMove_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GripperMove_SendGoal_Request_goal goal_id(::action_interface::action::GripperMove_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GripperMove_SendGoal_Request_goal(msg_);
  }

private:
  ::action_interface::action::GripperMove_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_SendGoal_Request>()
{
  return action_interface::action::builder::Init_GripperMove_SendGoal_Request_goal_id();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_SendGoal_Response_stamp
{
public:
  explicit Init_GripperMove_SendGoal_Response_stamp(::action_interface::action::GripperMove_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::action_interface::action::GripperMove_SendGoal_Response stamp(::action_interface::action::GripperMove_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_SendGoal_Response msg_;
};

class Init_GripperMove_SendGoal_Response_accepted
{
public:
  Init_GripperMove_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GripperMove_SendGoal_Response_stamp accepted(::action_interface::action::GripperMove_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_GripperMove_SendGoal_Response_stamp(msg_);
  }

private:
  ::action_interface::action::GripperMove_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_SendGoal_Response>()
{
  return action_interface::action::builder::Init_GripperMove_SendGoal_Response_accepted();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_GetResult_Request_goal_id
{
public:
  Init_GripperMove_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_interface::action::GripperMove_GetResult_Request goal_id(::action_interface::action::GripperMove_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_GetResult_Request>()
{
  return action_interface::action::builder::Init_GripperMove_GetResult_Request_goal_id();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_GetResult_Response_result
{
public:
  explicit Init_GripperMove_GetResult_Response_result(::action_interface::action::GripperMove_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::action_interface::action::GripperMove_GetResult_Response result(::action_interface::action::GripperMove_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_GetResult_Response msg_;
};

class Init_GripperMove_GetResult_Response_status
{
public:
  Init_GripperMove_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GripperMove_GetResult_Response_result status(::action_interface::action::GripperMove_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_GripperMove_GetResult_Response_result(msg_);
  }

private:
  ::action_interface::action::GripperMove_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_GetResult_Response>()
{
  return action_interface::action::builder::Init_GripperMove_GetResult_Response_status();
}

}  // namespace action_interface


namespace action_interface
{

namespace action
{

namespace builder
{

class Init_GripperMove_FeedbackMessage_feedback
{
public:
  explicit Init_GripperMove_FeedbackMessage_feedback(::action_interface::action::GripperMove_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::action_interface::action::GripperMove_FeedbackMessage feedback(::action_interface::action::GripperMove_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_interface::action::GripperMove_FeedbackMessage msg_;
};

class Init_GripperMove_FeedbackMessage_goal_id
{
public:
  Init_GripperMove_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GripperMove_FeedbackMessage_feedback goal_id(::action_interface::action::GripperMove_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GripperMove_FeedbackMessage_feedback(msg_);
  }

private:
  ::action_interface::action::GripperMove_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_interface::action::GripperMove_FeedbackMessage>()
{
  return action_interface::action::builder::Init_GripperMove_FeedbackMessage_goal_id();
}

}  // namespace action_interface

#endif  // ACTION_INTERFACE__ACTION__DETAIL__GRIPPER_MOVE__BUILDER_HPP_
