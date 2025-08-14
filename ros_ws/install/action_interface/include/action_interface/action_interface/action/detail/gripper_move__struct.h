// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from action_interface:action/GripperMove.idl
// generated code does not contain a copyright notice

#ifndef ACTION_INTERFACE__ACTION__DETAIL__GRIPPER_MOVE__STRUCT_H_
#define ACTION_INTERFACE__ACTION__DETAIL__GRIPPER_MOVE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_Goal
{
  int32_t action;
} action_interface__action__GripperMove_Goal;

// Struct for a sequence of action_interface__action__GripperMove_Goal.
typedef struct action_interface__action__GripperMove_Goal__Sequence
{
  action_interface__action__GripperMove_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_Result
{
  bool complete;
} action_interface__action__GripperMove_Result;

// Struct for a sequence of action_interface__action__GripperMove_Result.
typedef struct action_interface__action__GripperMove_Result__Sequence
{
  action_interface__action__GripperMove_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_Feedback
{
  bool running;
} action_interface__action__GripperMove_Feedback;

// Struct for a sequence of action_interface__action__GripperMove_Feedback.
typedef struct action_interface__action__GripperMove_Feedback__Sequence
{
  action_interface__action__GripperMove_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "action_interface/action/detail/gripper_move__struct.h"

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  action_interface__action__GripperMove_Goal goal;
} action_interface__action__GripperMove_SendGoal_Request;

// Struct for a sequence of action_interface__action__GripperMove_SendGoal_Request.
typedef struct action_interface__action__GripperMove_SendGoal_Request__Sequence
{
  action_interface__action__GripperMove_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} action_interface__action__GripperMove_SendGoal_Response;

// Struct for a sequence of action_interface__action__GripperMove_SendGoal_Response.
typedef struct action_interface__action__GripperMove_SendGoal_Response__Sequence
{
  action_interface__action__GripperMove_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} action_interface__action__GripperMove_GetResult_Request;

// Struct for a sequence of action_interface__action__GripperMove_GetResult_Request.
typedef struct action_interface__action__GripperMove_GetResult_Request__Sequence
{
  action_interface__action__GripperMove_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "action_interface/action/detail/gripper_move__struct.h"

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_GetResult_Response
{
  int8_t status;
  action_interface__action__GripperMove_Result result;
} action_interface__action__GripperMove_GetResult_Response;

// Struct for a sequence of action_interface__action__GripperMove_GetResult_Response.
typedef struct action_interface__action__GripperMove_GetResult_Response__Sequence
{
  action_interface__action__GripperMove_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "action_interface/action/detail/gripper_move__struct.h"

/// Struct defined in action/GripperMove in the package action_interface.
typedef struct action_interface__action__GripperMove_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  action_interface__action__GripperMove_Feedback feedback;
} action_interface__action__GripperMove_FeedbackMessage;

// Struct for a sequence of action_interface__action__GripperMove_FeedbackMessage.
typedef struct action_interface__action__GripperMove_FeedbackMessage__Sequence
{
  action_interface__action__GripperMove_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_interface__action__GripperMove_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ACTION_INTERFACE__ACTION__DETAIL__GRIPPER_MOVE__STRUCT_H_
